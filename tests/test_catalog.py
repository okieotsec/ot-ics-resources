# SPDX-License-Identifier: MIT
"""Tests for the catalog rules and the README generator (standard library only)."""
import copy
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_readme  # noqa: E402
import catalog  # noqa: E402


def sample():
    return {
        "schema_version": 2, "title": "Test", "research_date": "2026-10-12",
        "counts": {"free": 1, "paid": 1, "total": 2},
        "resources": [
            {"id": "R001", "category": "Basics", "title": "Free one", "url": "https://example.org/a", "level": "Foundation",
             "summary": "S", "practical_use": "U", "cost_group": "free", "cost": "$0", "access": "Free",
             "last_reviewed": "2026-10-12", "verification": "V", "access_class": "public_free", "audience_tags": ["foundation"]},
            {"id": "R002", "category": "Paid", "title": "Paid one", "url": "https://example.org/b", "level": "Practitioner",
             "summary": "S", "practical_use": "U", "cost_group": "paid", "cost": "$20", "access": "One-time",
             "last_reviewed": "2026-10-12", "verification": "V", "access_class": "paid", "audience_tags": ["practitioner"]},
        ],
    }


class RealCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = catalog.load()

    def test_the_committed_catalog_is_valid(self):
        errors, _ = catalog.validate(self.data)
        self.assertEqual(errors, [])

    def test_the_original_88_ids_are_all_still_there_and_the_ids_are_in_order(self):
        ids = [r["id"] for r in self.data["resources"]]
        self.assertTrue({f"R{n:03d}" for n in range(1, 89)} <= set(ids))
        self.assertEqual(ids, sorted(ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_primary_url_is_https_with_a_host(self):
        for r in self.data["resources"]:
            self.assertTrue(catalog.valid_url(r["url"]), r["id"])

    def test_free_entries_cost_nothing_and_paid_entries_do(self):
        for r in self.data["resources"]:
            self.assertEqual(r["cost"] == "$0", r["cost_group"] == "free", r["id"])

    def test_every_entry_is_rendered_exactly_once_as_a_table_row_and_as_a_card(self):
        text = build_readme.render(self.data)
        for r in self.data["resources"]:
            self.assertEqual(len(re.findall(rf"^\| {r['id']} \|", text, re.M)), 1, r["id"])
            self.assertEqual(len(re.findall(rf"^#### {r['id']} · ", text, re.M)), 1, r["id"])

    def test_free_entries_come_before_the_paid_section(self):
        text = build_readme.render(self.data)
        self.assertLess(text.index("## Free resources"), text.index("## Affordable paid resources"))
        for r in self.data["resources"]:
            position = text.index(f"#### {r['id']} · ")
            before_paid = position < text.index("## Affordable paid resources")
            self.assertEqual(before_paid, r["cost_group"] == "free", r["id"])

    def test_the_committed_readme_is_current_and_has_no_unresolved_placeholders(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(text, build_readme.render(self.data))
        self.assertIsNone(re.search(r"\{(research_date|free_count|paid_count|total_count|category_count|contents|glance|catalog)\}", text))

    def test_every_topic_link_points_at_a_heading_that_exists(self):
        text = build_readme.render(self.data)
        headings = {build_readme.slug(m) for m in re.findall(r"^#{2,3} (.+)$", text, re.M)}
        for anchor in re.findall(r"\]\(#([^)]+)\)", text):
            self.assertIn(anchor, headings, anchor)


class ValidationTests(unittest.TestCase):
    def problems(self, change):
        data = sample()
        change(data)
        errors, _ = catalog.validate(data)
        return errors

    def test_a_good_catalog_passes(self):
        self.assertEqual(catalog.validate(sample())[0], [])

    def test_each_rule_catches_its_own_mistake(self):
        cases = {
            "a duplicate id": lambda d: d["resources"][1].update(id="R001"),
            "a bad id": lambda d: d["resources"][0].update(id="X1"),
            "a plain http link": lambda d: d["resources"][0].update(url="http://example.org/a"),
            "a link with a password": lambda d: d["resources"][0].update(url="https://user:pw@example.org/a"),
            "a link with a space": lambda d: d["resources"][0].update(url="https://example.org/a b"),
            "a javascript link": lambda d: d["resources"][0].update(url="javascript:alert(1)"),
            "a free entry that costs money": lambda d: d["resources"][0].update(cost="$5"),
            "a paid entry that costs nothing": lambda d: d["resources"][1].update(cost="$0"),
            "a paid entry with a free class": lambda d: d["resources"][1].update(access_class="public_free"),
            "a free entry with a paid class": lambda d: d["resources"][0].update(access_class="paid"),
            "an unknown access class": lambda d: d["resources"][0].update(access_class="free-ish"),
            "stale counts": lambda d: d.update(counts={"free": 5, "paid": 1, "total": 6}),
            "a wrong schema version": lambda d: d.update(schema_version=1),
            "a bad date": lambda d: d["resources"][0].update(last_reviewed="yesterday"),
            "empty audience tags": lambda d: d["resources"][0].update(audience_tags=[]),
            "an upper-case tag": lambda d: d["resources"][0].update(audience_tags=["Foundation"]),
            "a missing field": lambda d: d["resources"][0].pop("summary"),
            "an empty text field": lambda d: d["resources"][0].update(summary="  "),
            "a non-boolean recommended flag": lambda d: d["resources"][0].update(recommended="yes"),
            "a bad related link": lambda d: d["resources"][0].update(related_url="ftp://example.org"),
            "no resources": lambda d: d.update(resources=[]),
        }
        for label, change in cases.items():
            with self.subTest(label):
                self.assertTrue(self.problems(change), label)

    def test_the_count_can_grow_without_a_code_change(self):
        data = sample()
        extra = copy.deepcopy(data["resources"][0])
        extra["id"], extra["url"] = "R003", "https://example.org/c"
        data["resources"].append(extra)
        data["counts"] = {"free": 2, "paid": 1, "total": 3}
        self.assertEqual(catalog.validate(data)[0], [])

    def test_a_shared_url_is_a_note_not_an_error(self):
        data = sample()
        data["resources"][1]["url"] = data["resources"][0]["url"]
        errors, warnings = catalog.validate(data)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)


class RenderingTests(unittest.TestCase):
    def test_resource_text_cannot_inject_markup_or_break_a_table(self):
        data = sample()
        data["resources"][0]["title"] = "Evil | <img src=x onerror=1> [x](javascript:alert(1)) *bold*"
        data["resources"][0]["summary"] = "<script>alert(1)</script> | pipe"
        text = build_readme.render(data)
        self.assertIsNone(re.search(r"(?<!\\)<script", text))          # only an escaped, inert form may appear
        self.assertIsNone(re.search(r"(?<!\\)<img src=x", text))
        self.assertIn("Evil \\| \\<img", text)
        table_row = next(line for line in text.splitlines() if line.startswith("| R001 |"))
        self.assertEqual(len(re.findall(r"(?<!\\)\|", table_row)), 5)

    def test_slugs_match_what_github_makes(self):
        self.assertEqual(build_readme.slug("Labs and protocol tooling"), "labs-and-protocol-tooling")
        self.assertEqual(build_readme.slug("Vulnerability management and prioritization"),
                         "vulnerability-management-and-prioritization")
        self.assertEqual(build_readme.slug("Q&A: what?"), "qa-what")

    def test_generation_is_deterministic(self):
        data = catalog.load()
        self.assertEqual(build_readme.render(data), build_readme.render(json.loads(json.dumps(data))))


if __name__ == "__main__":
    unittest.main()

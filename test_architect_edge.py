#!/usr/bin/env python3
"""
Additional tests for Pipeline Architect — Edge Cases & Integration.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from architect import (
    ArchitectConcept,
    ArchitectResult,
    PipelineArchitect,
    SequentialThinkingEnforcer,
    QualityScorer,
    QualityScore,
    ThinkingChain,
    ThinkingStep,
    SKILL_CATEGORIES,
    CONNECTORS,
)


def make_concept(name="Test", purpose="Build a pipeline", **kwargs):
    """Helper to create a concept with defaults."""
    defaults = {
        "inputs": [],
        "outputs": [],
        "domain": "engineering",
        "quality_target": 9.0,
        "complexity": 5,
        "required_skills": [],
        "required_connectors": [],
    }
    defaults.update(kwargs)
    return ArchitectConcept(name=name, purpose=purpose, **defaults)


class TestArchitectEdgeCases:
    def test_empty_concept(self):
        architect = PipelineArchitect()
        concept = make_concept(purpose="")
        result = architect.architect(concept)
        assert result is not None

    def test_simple_concept(self):
        architect = PipelineArchitect()
        concept = make_concept(purpose="Create a simple pipeline")
        result = architect.architect(concept)
        assert result is not None

    def test_complex_concept(self):
        architect = PipelineArchitect()
        concept = make_concept(
            purpose="Build a multi-stage CI/CD pipeline with security scanning",
            complexity=8,
        )
        result = architect.architect(concept)
        assert result is not None

    def test_with_inputs_outputs(self):
        architect = PipelineArchitect()
        concept = make_concept(
            purpose="Transform data",
            inputs=["data.csv"],
            outputs=["report.pdf"],
        )
        result = architect.architect(concept)
        assert result is not None


class TestSequentialThinking:
    def test_create_chain(self):
        enforcer = SequentialThinkingEnforcer()
        chain = enforcer.create_chain("test goal")
        assert chain is not None

    def test_chain_has_steps(self):
        enforcer = SequentialThinkingEnforcer()
        chain = enforcer.create_chain("test")
        assert len(chain.steps) > 0


class TestQualityScorer:
    def test_scorer_create(self):
        scorer = QualityScorer()
        assert scorer is not None


class TestConstants:
    def test_skill_categories(self):
        assert len(SKILL_CATEGORIES) > 0

    def test_connectors(self):
        assert len(CONNECTORS) > 0


class TestIntegration:
    def test_concept_create(self):
        concept = make_concept(purpose="test")
        assert concept.name == "Test"

    def test_concept_with_inputs(self):
        concept = make_concept(
            purpose="Transform data",
            inputs=["data.csv"],
            outputs=["report.pdf"],
        )
        assert "data.csv" in concept.inputs


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

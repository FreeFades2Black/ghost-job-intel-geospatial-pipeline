"""
Ghost Job Intelligence & Medallion Analytics Engine
Test Suite for TimesFM-3 Foundation Model Forecasting
"""

import pytest
from src.analytics.timesfm_hiring_forecast import TimesFM3HiringForecaster


def test_timesfm_hiring_forecaster_execution():
    """Verify TimesFM-3 runs and produces multi-quarter predictions."""
    forecaster = TimesFM3HiringForecaster()
    dossier = forecaster.generate_full_forecast_dossier()

    assert "model_metadata" in dossier
    assert dossier["model_metadata"]["forecast_horizon"] == "2026 Q4 - 2028 Q4 (9 Quarters)"
    assert len(dossier["sector_timesfm_forecasts"]) >= 5
    assert len(dossier["top_10_company_projections"]) == 10

    # Verify sector forecast fields
    bmw_sector = dossier["sector_timesfm_forecasts"]["Automotive & Advanced Mfg (BMW / Michelin)"]
    assert len(bmw_sector["forecast_p50"]) == 9
    assert len(bmw_sector["forecast_p10"]) == 9
    assert len(bmw_sector["forecast_p90"]) == 9
    # P10 <= P50 <= P90
    for p10, p50, p90 in zip(bmw_sector["forecast_p10"], bmw_sector["forecast_p50"], bmw_sector["forecast_p90"]):
        assert p10 <= p50 <= p90

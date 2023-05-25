import pandas as pd
import pandera as pa
from pandera.typing import Index, DataFrame, Series
from datetime import datetime
from pandera import dtypes


class InputSchema:
    class GlobalTempSchema(pa.SchemaModel):
        dt: Series[pa.DateTime] = pa.Field(coerce=True)
        LandAverageTemperature: Series[float] = pa.Field(coerce=True, nullable=True)
        LandAverageTemperatureUncertainty: Series[float] = pa.Field(
            coerce=True, nullable=True
        )
        LandMaxTemperature: Series[float] = pa.Field(coerce=True, nullable=True)
        LandMaxTemperatureUncertainty: Series[float] = pa.Field(
            coerce=True, nullable=True
        )
        LandMinTemperatureUncertainty: Series[float] = pa.Field(
            coerce=True, nullable=True
        )
        LandAndOceanAverageTemperature: Series[float] = pa.Field(
            coerce=True, nullable=True
        )
        LandAndOceanAverageTemperatureUncertainty: Series[float] = pa.Field(
            coerce=True, nullable=True
        )

    class GlobalLandTemperature(pa.SchemaModel):
        dt: Series[pa.DateTime] = pa.Field(coerce=True)
        AverageTemperature: Series[float] = pa.Field(coerce=True, nullable=True)
        AverageTemperatureUncertainty: Series[float] = pa.Field(
            coerce=True, nullable=True
        )
        City: Series[str] = pa.Field(coerce=True, nullable=True)
        Country: Series[str] = pa.Field(coerce=True, nullable=True)
        Latitude: Series[str] = pa.Field(coerce=True, nullable=True)
        Longitude: Series[str] = pa.Field(coerce=True, nullable=True)


class OutputSchema:
    class GlobalTempSchema(InputSchema.GlobalTempSchema):
        pass

    class GlobalLandTemperature(InputSchema.GlobalLandTemperature):
        pass


@pa.check_types
def transform_globaltempschema(
    df: DataFrame[InputSchema.GlobalTempSchema],
) -> DataFrame[OutputSchema.GlobalTempSchema]:
    return df


@pa.check_types
def transform_globallandtemp(
    df: DataFrame[InputSchema.GlobalLandTemperature],
) -> DataFrame[OutputSchema.GlobalLandTemperature]:
    return df

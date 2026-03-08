## Moved in Pydantic V2[¶](https://docs.pydantic.dev/latest/migration/#moved-in-pydantic-v2)
Pydantic V1 | Pydantic V2
---|---
`pydantic.BaseSettings` | [`pydantic_settings.BaseSettings`](https://docs.pydantic.dev/latest/migration/#basesettings-has-moved-to-pydantic-settings)
`pydantic.color` | [`pydantic_extra_types.color`](https://docs.pydantic.dev/latest/api/pydantic_extra_types_color/#pydantic_extra_types.color)
`pydantic.types.PaymentCardBrand` | [`pydantic_extra_types.PaymentCardBrand`](https://docs.pydantic.dev/latest/migration/#color-and-payment-card-numbers-moved-to-pydantic-extra-types)
`pydantic.types.PaymentCardNumber` | [`pydantic_extra_types.PaymentCardNumber`](https://docs.pydantic.dev/latest/migration/#color-and-payment-card-numbers-moved-to-pydantic-extra-types)
`pydantic.utils.version_info` | [`pydantic.version.version_info`](https://docs.pydantic.dev/latest/api/version/#pydantic.version.version_info)
`pydantic.error_wrappers.ValidationError` | [`pydantic.ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)
`pydantic.utils.to_camel` | [`pydantic.alias_generators.to_pascal`](https://docs.pydantic.dev/latest/api/config/#pydantic.alias_generators.to_pascal)
`pydantic.utils.to_lower_camel` | [`pydantic.alias_generators.to_camel`](https://docs.pydantic.dev/latest/api/config/#pydantic.alias_generators.to_camel)
`pydantic.PyObject` | [`pydantic.ImportString`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ImportString)

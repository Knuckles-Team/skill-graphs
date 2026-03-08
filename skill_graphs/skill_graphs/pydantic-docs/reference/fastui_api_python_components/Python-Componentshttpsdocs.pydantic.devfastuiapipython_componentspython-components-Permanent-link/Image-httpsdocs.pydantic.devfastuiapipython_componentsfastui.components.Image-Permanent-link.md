##  Image [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image "Permanent link")
Bases: `BaseModel`
Image container component.
###  src `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image.src "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)src: str

```

The URL of the image to display.
###  alt `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image.alt "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)alt: str | None = None

```

Optional alt text for the image.
###  width `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image.width "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)width: str | int | None = None

```

Optional width used to display the image.
###  height `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image.height "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)height: str | int | None = None

```

Optional height used to display the image.
###  referrer_policy `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image.referrer_policy "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)referrer_policy: Literal['no-referrer', 'no-referrer-when-downgrade', 'origin', 'origin-when-cross-origin', 'same-origin', 'strict-origin', 'strict-origin-when-cross-origin', 'unsafe-url'] | None = None

```

Optional referrer policy for the image. Specifies what information to send when fetching the image.
For more info, see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy.
###  loading `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image.loading "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)loading: Literal['eager', 'lazy'] | None = None

```

Optional loading strategy for the image.
###  on_click `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image.on_click "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)on_click: AnyEvent | None = None

```

Optional event to trigger when the image is clicked.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the image's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Image.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Image'] = 'Image'

```

The type of the component. Always 'Image'.

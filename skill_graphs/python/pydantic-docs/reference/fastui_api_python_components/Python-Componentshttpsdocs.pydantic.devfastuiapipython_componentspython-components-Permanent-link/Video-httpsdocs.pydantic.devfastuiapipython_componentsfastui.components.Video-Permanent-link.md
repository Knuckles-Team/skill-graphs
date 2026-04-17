##  Video [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video "Permanent link")
Bases: `BaseModel`
Video component that displays a video or multiple videos.
###  sources `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.sources "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)sources: list[AnyUrl]

```

List of URLs to the video sources.
###  autoplay `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.autoplay "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)autoplay: bool | None = None

```

Optional flag to enable autoplay for the video.
###  controls `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.controls "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)controls: bool | None = None

```

Optional flag to enable controls (pause, play, etc) for the video.
###  loop `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.loop "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)loop: bool | None = None

```

Optional flag to enable looping for the video.
###  muted `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.muted "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)muted: bool | None = None

```

Optional flag to mute the video.
###  poster `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.poster "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)poster: AnyUrl | None = None

```

Optional URL to an image to display as the video poster (what is shown when the video is loading or until the user plays it).
###  width `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.width "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)width: str | int | None = None

```

Optional width used to display the video.
###  height `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.height "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)height: str | int | None = None

```

Optional height used to display the video.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the video's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Video.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Video'] = 'Video'

```

The type of the component. Always 'Video'.

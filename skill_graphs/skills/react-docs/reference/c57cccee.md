* [`tabIndex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex): A number. Overrides the default Tab button behavior. [Avoid using values other than `-1` and `0`.](https://www.tpgi.com/using-the-tabindex-attribute/)
* [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title): A string. Specifies the tooltip text for the element.
* [`translate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/translate): Either `'yes'` or `'no'`. Passing `'no'` excludes the element content from being translated.

You can also pass custom attributes as props, for example `mycustomprop="someValue"`. This can be useful when integrating with third-party libraries. The custom attribute name must be lowercase and must not start with `on`. The value will be converted to a string. If you pass `null` or `undefined`, the custom attribute will be removed.

These events fire only for the [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form) elements:

* [`onReset`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/reset_event): An [`Event` handler](#event-handler) function. Fires when a form gets reset.
* `onResetCapture`: A version of `onReset` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onSubmit`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit_event): An [`Event` handler](#event-handler) function. Fires when a form gets submitted.
* `onSubmitCapture`: A version of `onSubmit` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)

These events fire only for the [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog) elements. Unlike browser events, they bubble in React:

* [`onCancel`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/cancel_event): An [`Event` handler](#event-handler) function. Fires when the user tries to dismiss the dialog.
* `onCancelCapture`: A version of `onCancel` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onClose`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close_event): An [`Event` handler](#event-handler) function. Fires when a dialog has been closed.
* `onCloseCapture`: A version of `onClose` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)

These events fire only for the [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) elements. Unlike browser events, they bubble in React:

* [`onToggle`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDetailsElement/toggle_event): An [`Event` handler](#event-handler) function. Fires when the user toggles the details.
* `onToggleCapture`: A version of `onToggle` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)

These events fire for [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img), [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe), [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object), [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed), [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), and [SVG ` `](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/SVG_Image_Tag) elements. Unlike browser events, they bubble in React:

* `onLoad`: An [`Event` handler](#event-handler) function. Fires when the resource has loaded.
* `onLoadCapture`: A version of `onLoad` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onError`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/error_event): An [`Event` handler](#event-handler) function. Fires when the resource could not be loaded.
* `onErrorCapture`: A version of `onError` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)

These events fire for resources like [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio) and [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video). Unlike browser events, they bubble in React:

* [`onAbort`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/abort_event): An [`Event` handler](#event-handler) function. Fires when the resource has not fully loaded, but not due to an error.
* `onAbortCapture`: A version of `onAbort` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onCanPlay`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/canplay_event): An [`Event` handler](#event-handler) function. Fires when there's enough data to start playing, but not enough to play to the end without buffering.
* `onCanPlayCapture`: A version of `onCanPlay` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onCanPlayThrough`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/canplaythrough_event): An [`Event` handler](#event-handler) function. Fires when there's enough data that it's likely possible to start playing without buffering until the end.
* `onCanPlayThroughCapture`: A version of `onCanPlayThrough` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onDurationChange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/durationchange_event): An [`Event` handler](#event-handler) function. Fires when the media duration has updated.
* `onDurationChangeCapture`: A version of `onDurationChange` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onEmptied`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/emptied_event): An [`Event` handler](#event-handler) function. Fires when the media has become empty.
* `onEmptiedCapture`: A version of `onEmptied` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onEncrypted`](https://w3c.github.io/encrypted-media/#dom-evt-encrypted): An [`Event` handler](#event-handler) function. Fires when the browser encounters encrypted media.
* `onEncryptedCapture`: A version of `onEncrypted` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onEnded`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ended_event): An [`Event` handler](#event-handler) function. Fires when the playback stops because there's nothing left to play.
* `onEndedCapture`: A version of `onEnded` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onError`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/error_event): An [`Event` handler](#event-handler) function. Fires when the resource could not be loaded.
* `onErrorCapture`: A version of `onError` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onLoadedData`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadeddata_event): An [`Event` handler](#event-handler) function. Fires when the current playback frame has loaded.
* `onLoadedDataCapture`: A version of `onLoadedData` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onLoadedMetadata`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadedmetadata_event): An [`Event` handler](#event-handler) function. Fires when metadata has loaded.
* `onLoadedMetadataCapture`: A version of `onLoadedMetadata` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onLoadStart`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadstart_event): An [`Event` handler](#event-handler) function. Fires when the browser started loading the resource.
* `onLoadStartCapture`: A version of `onLoadStart` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onPause`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/pause_event): An [`Event` handler](#event-handler) function. Fires when the media was paused.
* `onPauseCapture`: A version of `onPause` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onPlay`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/play_event): An [`Event` handler](#event-handler) function. Fires when the media is no longer paused.
* `onPlayCapture`: A version of `onPlay` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onPlaying`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/playing_event): An [`Event` handler](#event-handler) function. Fires when the media starts or restarts playing.
* `onPlayingCapture`: A version of `onPlaying` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onProgress`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/progress_event): An [`Event` handler](#event-handler) function. Fires periodically while the resource is loading.
* `onProgressCapture`: A version of `onProgress` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onRateChange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ratechange_event): An [`Event` handler](#event-handler) function. Fires when playback rate changes.
* `onRateChangeCapture`: A version of `onRateChange` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* `onResize`: An [`Event` handler](#event-handler) function. Fires when video changes size.
* `onResizeCapture`: A version of `onResize` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onSeeked`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/seeked_event): An [`Event` handler](#event-handler) function. Fires when a seek operation completes.
* `onSeekedCapture`: A version of `onSeeked` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onSeeking`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/seeking_event): An [`Event` handler](#event-handler) function. Fires when a seek operation starts.
* `onSeekingCapture`: A version of `onSeeking` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onStalled`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/stalled_event): An [`Event` handler](#event-handler) function. Fires when the browser is waiting for data but it keeps not loading.
* `onStalledCapture`: A version of `onStalled` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onSuspend`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/suspend_event): An [`Event` handler](#event-handler) function. Fires when loading the resource was suspended.
* `onSuspendCapture`: A version of `onSuspend` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onTimeUpdate`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/timeupdate_event): An [`Event` handler](#event-handler) function. Fires when the current playback time updates.
* `onTimeUpdateCapture`: A version of `onTimeUpdate` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onVolumeChange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/volumechange_event): An [`Event` handler](#event-handler) function. Fires when the volume has changed.
* `onVolumeChangeCapture`: A version of `onVolumeChange` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onWaiting`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/waiting_event): An [`Event` handler](#event-handler) function. Fires when the playback stopped due to temporary lack of data.
* `onWaitingCapture`: A version of `onWaiting` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)

#### Caveats {/*common-caveats*/}

- You cannot pass both `children` and `dangerouslySetInnerHTML` at the same time.
- Some events (like `onAbort` and `onLoad`) don't bubble in the browser, but bubble in React.

---

### `ref` callback function {/*ref-callback*/}

Instead of a ref object (like the one returned by [`useRef`](/reference/react/useRef#manipulating-the-dom-with-a-ref)), you may pass a function to the `ref` attribute.

```js
 {
 console.log('Attached', node);

 return () => {
 console.log('Clean up', node)
 }
}}>
```

[See an example of using the `ref` callback.](/learn/manipulating-the-dom-with-refs#how-to-manage-a-list-of-refs-using-a-ref-callback)

When the ` ` DOM node is added to the screen, React will call your `ref` callback with the DOM `node` as the argument. When that ` ` DOM node is removed, React will call your the cleanup function returned from the callback.

React will also call your `ref` callback whenever you pass a *different* `ref` callback. In the above example, `(node) => { ... }` is a different function on every render. When your component re-renders, the *previous* function will be called with `null` as the argument, and the *next* function will be called with the DOM node.

#### Parameters {/*ref-callback-parameters*/}

* `node`: A DOM node. React will pass you the DOM node when the ref gets attached. Unless you pass the same function reference for the `ref` callback on every render, the callback will get temporarily cleanup and re-create during every re-render of the component.

#### React 19 added cleanup functions for `ref` callbacks. {/*react-19-added-cleanup-functions-for-ref-callbacks*/}

To support backwards compatibility, if a cleanup function is not returned from the `ref` callback, `node` will be called with `null` when the `ref` is detached. This behavior will be removed in a future version.

#### Returns {/*returns*/}

* **optional** `cleanup function`: When the `ref` is detached, React will call the cleanup function. If a function is not returned by the `ref` callback, React will call the callback again with `null` as the argument when the `ref` gets detached. This behavior will be removed in a future version.

#### Caveats {/*caveats*/}

* When Strict Mode is on, React will **run one extra development-only setup+cleanup cycle** before the first real setup. This is a stress-test that ensures that your cleanup logic "mirrors" your setup logic and that it stops or undoes whatever the setup is doing. If this causes a problem, implement the cleanup function.
* When you pass a *different* `ref` callback, React will call the *previous* callback's cleanup function if provided. If no cleanup function is defined, the `ref` callback will be called with `null` as the argument. The *next* function will be called with the DOM node.

---

### React event object {/*react-event-object*/}

Your event handlers will receive a *React event object.* It is also sometimes known as a "synthetic event".

```js
 {
 console.log(e); // React event object
}} />
```

It conforms to the same standard as the underlying DOM events, but fixes some browser inconsistencies.

Some React events do not map directly to the browser's native events. For example in `onMouseLeave`, `e.nativeEvent` will point to a `mouseout` event. The specific mapping is not part of the public API and may change in the future. If you need the underlying browser event for some reason, read it from `e.nativeEvent`.

#### Properties {/*react-event-object-properties*/}

React event objects implement some of the standard [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event) properties:

* [`bubbles`](https://developer.mozilla.org/en-US/docs/Web/API/Event/bubbles): A boolean. Returns whether the event bubbles through the DOM.
* [`cancelable`](https://developer.mozilla.org/en-US/docs/Web/API/Event/cancelable): A boolean. Returns whether the event can be canceled.
* [`currentTarget`](https://developer.mozilla.org/en-US/docs/Web/API/Event/currentTarget): A DOM node. Returns the node to which the current handler is attached in the React tree.
* [`defaultPrevented`](https://developer.mozilla.org/en-US/docs/Web/API/Event/defaultPrevented): A boolean. Returns whether `preventDefault` was called.
* [`eventPhase`](https://developer.mozilla.org/en-US/docs/Web/API/Event/eventPhase): A number. Returns which phase the event is currently in.
* [`isTrusted`](https://developer.mozilla.org/en-US/docs/Web/API/Event/isTrusted): A boolean. Returns whether the event was initiated by user.
* [`target`](https://developer.mozilla.org/en-US/docs/Web/API/Event/target): A DOM node. Returns the node on which the event has occurred (which could be a distant child).
* [`timeStamp`](https://developer.mozilla.org/en-US/docs/Web/API/Event/timeStamp): A number. Returns the time when the event occurred.

Additionally, React event objects provide these properties:

* `nativeEvent`: A DOM [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event). The original browser event object.

#### Methods {/*react-event-object-methods*/}

React event objects implement some of the standard [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event) methods:

* [`preventDefault()`](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault): Prevents the default browser action for the event.
* [`stopPropagation()`](https://developer.mozilla.org/en-US/docs/Web/API/Event/stopPropagation): Stops the event propagation through the React tree.

Additionally, React event objects provide these methods:

* `isDefaultPrevented()`: Returns a boolean value indicating whether `preventDefault` was called.
* `isPropagationStopped()`: Returns a boolean value indicating whether `stopPropagation` was called.
* `persist()`: Not used with React DOM. With React Native, call this to read event's properties after the event.
* `isPersistent()`: Not used with React DOM. With React Native, returns whether `persist` has been called.

#### Caveats {/*react-event-object-caveats*/}

* The values of `currentTarget`, `eventPhase`, `target`, and `type` reflect the values your React code expects. Under the hood, React attaches event handlers at the root, but this is not reflected in React event objects. For example, `e.currentTarget` may not be the same as the underlying `e.nativeEvent.currentTarget`. For polyfilled events, `e.type` (React event type) may differ from `e.nativeEvent.type` (underlying type).

---

### `AnimationEvent` handler function {/*animationevent-handler*/}

An event handler type for the [CSS animation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations) events.

```js
 console.log('onAnimationStart')}
 onAnimationIteration={e => console.log('onAnimationIteration')}
 onAnimationEnd={e => console.log('onAnimationEnd')}
/>
```

#### Parameters {/*animationevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent) properties:
 * [`animationName`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent/animationName)
 * [`elapsedTime`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent/elapsedTime)
 * [`pseudoElement`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent/pseudoElement)

---

### `ClipboardEvent` handler function {/*clipboadevent-handler*/}

An event handler type for the [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API) events.

```js
 console.log('onCopy')}
 onCut={e => console.log('onCut')}
 onPaste={e => console.log('onPaste')}
/>
```

#### Parameters {/*clipboadevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`ClipboardEvent`](https://developer.mozilla.org/en-US/docs/Web/API/ClipboardEvent) properties:

 * [`clipboardData`](https://developer.mozilla.org/en-US/docs/Web/API/ClipboardEvent/clipboardData)

---

### `CompositionEvent` handler function {/*compositionevent-handler*/}

An event handler type for the [input method editor (IME)](https://developer.mozilla.org/en-US/docs/Glossary/Input_method_editor) events.

```js
 console.log('onCompositionStart')}
 onCompositionUpdate={e => console.log('onCompositionUpdate')}
 onCompositionEnd={e => console.log('onCompositionEnd')}
/>
```

#### Parameters {/*compositionevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`CompositionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/CompositionEvent) properties:
 * [`data`](https://developer.mozilla.org/en-US/docs/Web/API/CompositionEvent/data)

---

### `DragEvent` handler function {/*dragevent-handler*/}

An event handler type for the [HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API) events.

```js
<>
 console.log('onDragStart')}
 onDragEnd={e => console.log('onDragEnd')}
 >
 Drag source

 console.log('onDragEnter')}
 onDragLeave={e => console.log('onDragLeave')}
 onDragOver={e => { e.preventDefault(); console.log('onDragOver'); }}
 onDrop={e => console.log('onDrop')}
 >
 Drop target

```

#### Parameters {/*dragevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`DragEvent`](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent) properties:
 * [`dataTransfer`](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/dataTransfer)

 It also includes the inherited [`MouseEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent) properties:

 * [`altKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/altKey)
 * [`button`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/button)
 * [`buttons`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/buttons)
 * [`ctrlKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/ctrlKey)
 * [`clientX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/clientX)
 * [`clientY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/clientY)
 * [`getModifierState(key)`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/getModifierState)
 * [`metaKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/metaKey)
 * [`movementX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/movementX)
 * [`movementY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/movementY)
 * [`pageX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageX)
 * [`pageY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageY)
 * [`relatedTarget`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/relatedTarget)
 * [`screenX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/screenX)
 * [`screenY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/screenY)
 * [`shiftKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/shiftKey)

 It also includes the inherited [`UIEvent`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent) properties:

 * [`detail`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail)
 * [`view`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/view)

---

### `FocusEvent` handler function {/*focusevent-handler*/}

An event handler type for the focus events.

```js
 console.log('onFocus')}
 onBlur={e => console.log('onBlur')}
/>
```

[See an example.](#handling-focus-events)

#### Parameters {/*focusevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`FocusEvent`](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent) properties:
 * [`relatedTarget`](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/relatedTarget)

 It also includes the inherited [`UIEvent`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent) properties:

 * [`detail`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail)
 * [`view`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/view)

---

### `Event` handler function {/*event-handler*/}

An event handler type for generic events.

#### Parameters {/*event-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with no additional properties.

---

### `InputEvent` handler function {/*inputevent-handler*/}

An event handler type for the `onBeforeInput` event.

```js
 console.log('onBeforeInput')} />
```

#### Parameters {/*inputevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`InputEvent`](https://developer.mozilla.org/en-US/docs/Web/API/InputEvent) properties:
 * [`data`](https://developer.mozilla.org/en-US/docs/Web/API/InputEvent/data)

---

### `KeyboardEvent` handler function {/*keyboardevent-handler*/}

An event handler type for keyboard events.

```js
 console.log('onKeyDown')}
 onKeyUp={e => console.log('onKeyUp')}
/>
```

[See an example.](#handling-keyboard-events)

#### Parameters {/*keyboardevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`KeyboardEvent`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent) properties:
 * [`altKey`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/altKey)
 * [`charCode`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/charCode)
 * [`code`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/code)
 * [`ctrlKey`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/ctrlKey)

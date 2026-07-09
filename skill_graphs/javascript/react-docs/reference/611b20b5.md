---
title: "Common components (e.g. )"
---

All built-in browser components, such as [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div), support some common props and events.

---

## Reference {/*reference*/}

### Common components (e.g. ` `) {/*common*/}

```js
 Some content
```

[See more examples below.](#usage)

#### Props {/*common-props*/}

These special React props are supported for all built-in components:

* `children`: A React node (an element, a string, a number, [a portal,](/reference/react-dom/createPortal) an empty node like `null`, `undefined` and booleans, or an array of other React nodes). Specifies the content inside the component. When you use JSX, you will usually specify the `children` prop implicitly by nesting tags like ` `.

* `dangerouslySetInnerHTML`: An object of the form `{ __html: ' some html ' }` with a raw HTML string inside. Overrides the [`innerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML) property of the DOM node and displays the passed HTML inside. This should be used with extreme caution! If the HTML inside isn't trusted (for example, if it's based on user data), you risk introducing an [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting) vulnerability. [Read more about using `dangerouslySetInnerHTML`.](#dangerously-setting-the-inner-html)

* `ref`: A ref object from [`useRef`](/reference/react/useRef) or [`createRef`](/reference/react/createRef), or a [`ref` callback function,](#ref-callback) or a string for [legacy refs.](https://reactjs.org/docs/refs-and-the-dom.html#legacy-api-string-refs) Your ref will be filled with the DOM element for this node. [Read more about manipulating the DOM with refs.](#manipulating-a-dom-node-with-a-ref)

* `suppressContentEditableWarning`: A boolean. If `true`, suppresses the warning that React shows for elements that both have `children` and `contentEditable={true}` (which normally do not work together). Use this if you're building a text input library that manages the `contentEditable` content manually.

* `suppressHydrationWarning`: A boolean. If you use [server rendering,](/reference/react-dom/server) normally there is a warning when the server and the client render different content. In some rare cases (like timestamps), it is very hard or impossible to guarantee an exact match. If you set `suppressHydrationWarning` to `true`, React will not warn you about mismatches in the attributes and the content of that element. It only works one level deep, and is intended to be used as an escape hatch. Don't overuse it. [Read about suppressing hydration errors.](/reference/react-dom/client/hydrateRoot#suppressing-unavoidable-hydration-mismatch-errors)

* `style`: An object with CSS styles, for example `{ fontWeight: 'bold', margin: 20 }`. Similarly to the DOM [`style`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) property, the CSS property names need to be written as `camelCase`, for example `fontWeight` instead of `font-weight`. You can pass strings or numbers as values. If you pass a number, like `width: 100`, React will automatically append `px` ("pixels") to the value unless it's a [unitless property.](https://github.com/facebook/react/blob/81d4ee9ca5c405dce62f64e61506b8e155f38d8d/packages/react-dom-bindings/src/shared/CSSProperty.js#L8-L57) We recommend using `style` only for dynamic styles where you don't know the style values ahead of time. In other cases, applying plain CSS classes with `className` is more efficient. [Read more about `className` and `style`.](#applying-css-styles)

These standard DOM props are also supported for all built-in components:

* [`accessKey`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/accesskey): A string. Specifies a keyboard shortcut for the element. [Not generally recommended.](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/accesskey#accessibility_concerns)
* [`aria-*`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes): ARIA attributes let you specify the accessibility tree information for this element. See [ARIA attributes](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes) for a complete reference. In React, all ARIA attribute names are exactly the same as in HTML.
* [`autoCapitalize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/autocapitalize): A string. Specifies whether and how the user input should be capitalized.
* [`className`](https://developer.mozilla.org/en-US/docs/Web/API/Element/className): A string. Specifies the element's CSS class name. [Read more about applying CSS styles.](#applying-css-styles)
* [`contentEditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/contenteditable): A boolean. If `true`, the browser lets the user edit the rendered element directly. This is used to implement rich text input libraries like [Lexical.](https://lexical.dev/) React warns if you try to pass React children to an element with `contentEditable={true}` because React will not be able to update its content after user edits.
* [`data-*`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/data-*): Data attributes let you attach some string data to the element, for example `data-fruit="banana"`. In React, they are not commonly used because you would usually read data from props or state instead.
* [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/dir): Either `'ltr'` or `'rtl'`. Specifies the text direction of the element.
* [`draggable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable): A boolean. Specifies whether the element is draggable. Part of [HTML Drag and Drop API.](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
* [`enterKeyHint`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/enterKeyHint): A string. Specifies which action to present for the enter key on virtual keyboards.
* [`htmlFor`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/htmlFor): A string. For [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label) and [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output), lets you [associate the label with some control.](/reference/react-dom/components/input#providing-a-label-for-an-input) Same as [`for` HTML attribute.](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/for) React uses the standard DOM property names (`htmlFor`) instead of HTML attribute names.
* [`hidden`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden): A boolean or a string. Specifies whether the element should be hidden.
* [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id): A string. Specifies a unique identifier for this element, which can be used to find it later or connect it with other elements. Generate it with [`useId`](/reference/react/useId) to avoid clashes between multiple instances of the same component.
* [`is`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/is): A string. If specified, the component will behave like a [custom element.](/reference/react-dom/components#custom-html-elements)
* [`inputMode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode): A string. Specifies what kind of keyboard to display (for example, text, number or telephone).
* [`itemProp`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/itemprop): A string. Specifies which property the element represents for structured data crawlers.
* [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/lang): A string. Specifies the language of the element.
* [`onAnimationEnd`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationend_event): An [`AnimationEvent` handler](#animationevent-handler) function. Fires when a CSS animation completes.
* `onAnimationEndCapture`: A version of `onAnimationEnd` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onAnimationIteration`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationiteration_event): An [`AnimationEvent` handler](#animationevent-handler) function. Fires when an iteration of a CSS animation ends, and another one begins.
* `onAnimationIterationCapture`: A version of `onAnimationIteration` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onAnimationStart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationstart_event): An [`AnimationEvent` handler](#animationevent-handler) function. Fires when a CSS animation starts.
* `onAnimationStartCapture`: `onAnimationStart`, but fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onAuxClick`](https://developer.mozilla.org/en-US/docs/Web/API/Element/auxclick_event): A [`MouseEvent` handler](#mouseevent-handler) function. Fires when a non-primary pointer button was clicked.
* `onAuxClickCapture`: A version of `onAuxClick` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* `onBeforeInput`: An [`InputEvent` handler](#inputevent-handler) function. Fires before the value of an editable element is modified. React does *not* yet use the native [`beforeinput`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/beforeinput_event) event, and instead attempts to polyfill it using other events.
* `onBeforeInputCapture`: A version of `onBeforeInput` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* `onBlur`: A [`FocusEvent` handler](#focusevent-handler) function. Fires when an element lost focus. Unlike the built-in browser [`blur`](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event) event, in React the `onBlur` event bubbles.
* `onBlurCapture`: A version of `onBlur` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onClick`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event): A [`MouseEvent` handler](#mouseevent-handler) function. Fires when the primary button was clicked on the pointing device.
* `onClickCapture`: A version of `onClick` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onCompositionStart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/compositionstart_event): A [`CompositionEvent` handler](#compositionevent-handler) function. Fires when an [input method editor](https://developer.mozilla.org/en-US/docs/Glossary/Input_method_editor) starts a new composition session.
* `onCompositionStartCapture`: A version of `onCompositionStart` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onCompositionEnd`](https://developer.mozilla.org/en-US/docs/Web/API/Element/compositionend_event): A [`CompositionEvent` handler](#compositionevent-handler) function. Fires when an [input method editor](https://developer.mozilla.org/en-US/docs/Glossary/Input_method_editor) completes or cancels a composition session.
* `onCompositionEndCapture`: A version of `onCompositionEnd` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onCompositionUpdate`](https://developer.mozilla.org/en-US/docs/Web/API/Element/compositionupdate_event): A [`CompositionEvent` handler](#compositionevent-handler) function. Fires when an [input method editor](https://developer.mozilla.org/en-US/docs/Glossary/Input_method_editor) receives a new character.
* `onCompositionUpdateCapture`: A version of `onCompositionUpdate` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onContextMenu`](https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event): A [`MouseEvent` handler](#mouseevent-handler) function. Fires when the user tries to open a context menu.
* `onContextMenuCapture`: A version of `onContextMenu` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onCopy`](https://developer.mozilla.org/en-US/docs/Web/API/Element/copy_event): A [`ClipboardEvent` handler](#clipboardevent-handler) function. Fires when the user tries to copy something into the clipboard.
* `onCopyCapture`: A version of `onCopy` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onCut`](https://developer.mozilla.org/en-US/docs/Web/API/Element/cut_event): A [`ClipboardEvent` handler](#clipboardevent-handler) function. Fires when the user tries to cut something into the clipboard.
* `onCutCapture`: A version of `onCut` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* `onDoubleClick`: A [`MouseEvent` handler](#mouseevent-handler) function. Fires when the user clicks twice. Corresponds to the browser [`dblclick` event.](https://developer.mozilla.org/en-US/docs/Web/API/Element/dblclick_event)
* `onDoubleClickCapture`: A version of `onDoubleClick` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onDrag`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/drag_event): A [`DragEvent` handler](#dragevent-handler) function. Fires while the user is dragging something.
* `onDragCapture`: A version of `onDrag` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onDragEnd`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragend_event): A [`DragEvent` handler](#dragevent-handler) function. Fires when the user stops dragging something.
* `onDragEndCapture`: A version of `onDragEnd` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onDragEnter`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragenter_event): A [`DragEvent` handler](#dragevent-handler) function. Fires when the dragged content enters a valid drop target.
* `onDragEnterCapture`: A version of `onDragEnter` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onDragOver`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragover_event): A [`DragEvent` handler](#dragevent-handler) function. Fires on a valid drop target while the dragged content is dragged over it. You must call `e.preventDefault()` here to allow dropping.
* `onDragOverCapture`: A version of `onDragOver` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onDragStart`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragstart_event): A [`DragEvent` handler](#dragevent-handler) function. Fires when the user starts dragging an element.
* `onDragStartCapture`: A version of `onDragStart` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onDrop`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/drop_event): A [`DragEvent` handler](#dragevent-handler) function. Fires when something is dropped on a valid drop target.
* `onDropCapture`: A version of `onDrop` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* `onFocus`: A [`FocusEvent` handler](#focusevent-handler) function. Fires when an element receives focus. Unlike the built-in browser [`focus`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focus_event) event, in React the `onFocus` event bubbles.
* `onFocusCapture`: A version of `onFocus` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onGotPointerCapture`](https://developer.mozilla.org/en-US/docs/Web/API/Element/gotpointercapture_event): A [`PointerEvent` handler](#pointerevent-handler) function. Fires when an element programmatically captures a pointer.
* `onGotPointerCaptureCapture`: A version of `onGotPointerCapture` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onKeyDown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keydown_event): A [`KeyboardEvent` handler](#keyboardevent-handler) function. Fires when a key is pressed.
* `onKeyDownCapture`: A version of `onKeyDown` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onKeyPress`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keypress_event): A [`KeyboardEvent` handler](#keyboardevent-handler) function. Deprecated. Use `onKeyDown` or `onBeforeInput` instead.
* `onKeyPressCapture`: A version of `onKeyPress` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onKeyUp`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keyup_event): A [`KeyboardEvent` handler](#keyboardevent-handler) function. Fires when a key is released.
* `onKeyUpCapture`: A version of `onKeyUp` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onLostPointerCapture`](https://developer.mozilla.org/en-US/docs/Web/API/Element/lostpointercapture_event): A [`PointerEvent` handler](#pointerevent-handler) function. Fires when an element stops capturing a pointer.
* `onLostPointerCaptureCapture`: A version of `onLostPointerCapture` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onMouseDown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousedown_event): A [`MouseEvent` handler](#mouseevent-handler) function. Fires when the pointer is pressed down.
* `onMouseDownCapture`: A version of `onMouseDown` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onMouseEnter`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseenter_event): A [`MouseEvent` handler](#mouseevent-handler) function. Fires when the pointer moves inside an element. Does not have a capture phase. Instead, `onMouseLeave` and `onMouseEnter` propagate from the element being left to the one being entered.
* [`onMouseLeave`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseleave_event): A [`MouseEvent` handler](#mouseevent-handler) function. Fires when the pointer moves outside an element. Does not have a capture phase. Instead, `onMouseLeave` and `onMouseEnter` propagate from the element being left to the one being entered.
* [`onMouseMove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousemove_event): A [`MouseEvent` handler](#mouseevent-handler) function. Fires when the pointer changes coordinates.
* `onMouseMoveCapture`: A version of `onMouseMove` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onMouseOut`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseout_event): A [`MouseEvent` handler](#mouseevent-handler) function. Fires when the pointer moves outside an element, or if it moves into a child element.
* `onMouseOutCapture`: A version of `onMouseOut` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onMouseUp`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseup_event): A [`MouseEvent` handler](#mouseevent-handler) function. Fires when the pointer is released.
* `onMouseUpCapture`: A version of `onMouseUp` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onPointerCancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointercancel_event): A [`PointerEvent` handler](#pointerevent-handler) function. Fires when the browser cancels a pointer interaction.
* `onPointerCancelCapture`: A version of `onPointerCancel` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onPointerDown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerdown_event): A [`PointerEvent` handler](#pointerevent-handler) function. Fires when a pointer becomes active.
* `onPointerDownCapture`: A version of `onPointerDown` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onPointerEnter`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerenter_event): A [`PointerEvent` handler](#pointerevent-handler) function. Fires when a pointer moves inside an element. Does not have a capture phase. Instead, `onPointerLeave` and `onPointerEnter` propagate from the element being left to the one being entered.
* [`onPointerLeave`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerleave_event): A [`PointerEvent` handler](#pointerevent-handler) function. Fires when a pointer moves outside an element. Does not have a capture phase. Instead, `onPointerLeave` and `onPointerEnter` propagate from the element being left to the one being entered.
* [`onPointerMove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointermove_event): A [`PointerEvent` handler](#pointerevent-handler) function. Fires when a pointer changes coordinates.
* `onPointerMoveCapture`: A version of `onPointerMove` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onPointerOut`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerout_event): A [`PointerEvent` handler](#pointerevent-handler) function. Fires when a pointer moves outside an element, if the pointer interaction is cancelled, and [a few other reasons.](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerout_event)
* `onPointerOutCapture`: A version of `onPointerOut` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onPointerUp`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerup_event): A [`PointerEvent` handler](#pointerevent-handler) function. Fires when a pointer is no longer active.
* `onPointerUpCapture`: A version of `onPointerUp` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onPaste`](https://developer.mozilla.org/en-US/docs/Web/API/Element/paste_event): A [`ClipboardEvent` handler](#clipboardevent-handler) function. Fires when the user tries to paste something from the clipboard.
* `onPasteCapture`: A version of `onPaste` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onScroll`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scroll_event): An [`Event` handler](#event-handler) function. Fires when an element has been scrolled. This event does not bubble.
* `onScrollCapture`: A version of `onScroll` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onSelect`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/select_event): An [`Event` handler](#event-handler) function. Fires after the selection inside an editable element like an input changes. React extends the `onSelect` event to work for `contentEditable={true}` elements as well. In addition, React extends it to fire for empty selection and on edits (which may affect the selection).
* `onSelectCapture`: A version of `onSelect` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onTouchCancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchcancel_event): A [`TouchEvent` handler](#touchevent-handler) function. Fires when the browser cancels a touch interaction.
* `onTouchCancelCapture`: A version of `onTouchCancel` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onTouchEnd`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchend_event): A [`TouchEvent` handler](#touchevent-handler) function. Fires when one or more touch points are removed.
* `onTouchEndCapture`: A version of `onTouchEnd` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onTouchMove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchmove_event): A [`TouchEvent` handler](#touchevent-handler) function. Fires one or more touch points are moved.
* `onTouchMoveCapture`: A version of `onTouchMove` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onTouchStart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchstart_event): A [`TouchEvent` handler](#touchevent-handler) function. Fires when one or more touch points are placed.
* `onTouchStartCapture`: A version of `onTouchStart` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onTransitionEnd`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionend_event): A [`TransitionEvent` handler](#transitionevent-handler) function. Fires when a CSS transition completes.
* `onTransitionEndCapture`: A version of `onTransitionEnd` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`onWheel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/wheel_event): A [`WheelEvent` handler](#wheelevent-handler) function. Fires when the user rotates a wheel button.
* `onWheelCapture`: A version of `onWheel` that fires in the [capture phase.](/learn/responding-to-events#capture-phase-events)
* [`role`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles): A string. Specifies the element role explicitly for assistive technologies.
* [`slot`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles): A string. Specifies the slot name when using shadow DOM. In React, an equivalent pattern is typically achieved by passing JSX as props, for example ` } right={ } />`.
* [`spellCheck`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/spellcheck): A boolean or null. If explicitly set to `true` or `false`, enables or disables spellchecking.

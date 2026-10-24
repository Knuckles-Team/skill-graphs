#####  `nodeEventTarget.removeListener(type, listener[, options])`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetremovelistenertype-listener-options)
Added in: v14.5.0
  * `type`
  * `listener` [`<EventListener>`](https://nodejs.org/docs/latest/api/events.html#event-listener)
  * `options`
    * `capture`
  * Returns: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) this


Node.js-specific extension to the `EventTarget` class that removes the `listener` for the given `type`. The only difference between `removeListener()` and `removeEventListener()` is that `removeListener()` will return a reference to the `EventTarget`.

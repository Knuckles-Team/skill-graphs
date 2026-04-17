

This method allows mapping over the stream. The `fn` function will be called for every chunk in the stream. If the `fn` function returns a promise - that promise will be `await`ed before being passed to the result stream.
```
import { Readable } from 'node:stream';
import { Resolver } from 'node:dns/promises';

// With a synchronous mapper.
for await (const chunk of Readable.from([1, 2, 3, 4]).map((x) => x * 2)) {
  console.log(chunk); // 2, 4, 6, 8
}
// With an asynchronous mapper, making at most 2 queries at a time.
const resolver = new Resolver();
const dnsResults = Readable.from([
  'nodejs.org',
  'openjsf.org',
  'www.linuxfoundation.org',
]).map((domain) => resolver.resolve4(domain), { concurrency: 2 });
for await (const result of dnsResults) {
  console.log(result); // Logs the DNS result of resolver.resolve4.
}
copy
```

######  `readable.filter(fn[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readablefilterfn-options)
Added in: v17.4.0, v16.14.0History Version | Changes
---|---
v20.7.0, v18.19.0 | added `highWaterMark` in options.
Stability: 1 - Experimental
  * `fn`
    * `data`
    * `options`
      * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) aborted if the stream is destroyed allowing to abort the `fn` call early.
  * `options`
    * `concurrency` `fn` to call on the stream at once. **Default:** `1`.
    * `highWaterMark` **Default:** `concurrency * 2 - 1`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns: [`<Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) a stream filtered with the predicate `fn`.


This method allows filtering the stream. For each chunk in the stream the `fn` function will be called and if it returns a truthy value, the chunk will be passed to the result stream. If the `fn` function returns a promise - that promise will be `await`ed.
```
import { Readable } from 'node:stream';
import { Resolver } from 'node:dns/promises';

// With a synchronous predicate.
for await (const chunk of Readable.from([1, 2, 3, 4]).filter((x) => x > 2)) {
  console.log(chunk); // 3, 4
}
// With an asynchronous predicate, making at most 2 queries at a time.
const resolver = new Resolver();
const dnsResults = Readable.from([
  'nodejs.org',
  'openjsf.org',
  'www.linuxfoundation.org',
]).filter(async (domain) => {
  const { address } = await resolver.resolve4(domain, { ttl: true });
  return address.ttl > 60;
}, { concurrency: 2 });
for await (const result of dnsResults) {
  // Logs domains with more than 60 seconds on the resolved dns record.
  console.log(result);
}
copy
```

######  `readable.forEach(fn[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readableforeachfn-options)
Added in: v17.5.0, v16.15.0
Stability: 1 - Experimental
  * `fn`
    * `data`
    * `options`
      * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) aborted if the stream is destroyed allowing to abort the `fn` call early.
  * `options`
    * `concurrency` `fn` to call on the stream at once. **Default:** `1`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns:


This method allows iterating a stream. For each chunk in the stream the `fn` function will be called. If the `fn` function returns a promise - that promise will be `await`ed.
This method is different from `for await...of` loops in that it can optionally process chunks concurrently. In addition, a `forEach` iteration can only be stopped by having passed a `signal` option and aborting the related `AbortController` while `for await...of` can be stopped with `break` or `return`. In either case the stream will be destroyed.
This method is different from listening to the [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) event in that it uses the [`readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) event in the underlying machinery and can limit the number of concurrent `fn` calls.
```
import { Readable } from 'node:stream';
import { Resolver } from 'node:dns/promises';

// With a synchronous predicate.
for await (const chunk of Readable.from([1, 2, 3, 4]).filter((x) => x > 2)) {
  console.log(chunk); // 3, 4
}
// With an asynchronous predicate, making at most 2 queries at a time.
const resolver = new Resolver();
const dnsResults = Readable.from([
  'nodejs.org',
  'openjsf.org',
  'www.linuxfoundation.org',
]).map(async (domain) => {
  const { address } = await resolver.resolve4(domain, { ttl: true });
  return address;
}, { concurrency: 2 });
await dnsResults.forEach((result) => {
  // Logs result, similar to `for await (const result of dnsResults)`
  console.log(result);
});
console.log('done'); // Stream has finished
copy
```

######  `readable.toArray([options])`[#](https://nodejs.org/docs/latest/api/stream.html#readabletoarrayoptions)
Added in: v17.5.0, v16.15.0
Stability: 1 - Experimental
  * `options`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows cancelling the toArray operation if the signal is aborted.
  * Returns:


This method allows easily obtaining the contents of a stream.
As this method reads the entire stream into memory, it negates the benefits of streams. It's intended for interoperability and convenience, not as the primary way to consume streams.
```
import { Readable } from 'node:stream';
import { Resolver } from 'node:dns/promises';

await Readable.from([1, 2, 3, 4]).toArray(); // [1, 2, 3, 4]

const resolver = new Resolver();

// Make dns queries concurrently using .map and collect
// the results into an array using toArray
const dnsResults = await Readable.from([
  'nodejs.org',
  'openjsf.org',
  'www.linuxfoundation.org',
]).map(async (domain) => {
  const { address } = await resolver.resolve4(domain, { ttl: true });
  return address;
}, { concurrency: 2 }).toArray();
copy
```

######  `readable.some(fn[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readablesomefn-options)
Added in: v17.5.0, v16.15.0
Stability: 1 - Experimental
  * `fn`
    * `data`
    * `options`
      * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) aborted if the stream is destroyed allowing to abort the `fn` call early.
  * `options`
    * `concurrency` `fn` to call on the stream at once. **Default:** `1`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns: `true` if `fn` returned a truthy value for at least one of the chunks.


This method is similar to `Array.prototype.some` and calls `fn` on each chunk in the stream until the awaited return value is `true` (or any truthy value). Once an `fn` call on a chunk awaited return value is truthy, the stream is destroyed and the promise is fulfilled with `true`. If none of the `fn` calls on the chunks return a truthy value, the promise is fulfilled with `false`.
```
import { Readable } from 'node:stream';
import { stat } from 'node:fs/promises';

// With a synchronous predicate.
await Readable.from([1, 2, 3, 4]).some((x) => x > 2); // true
await Readable.from([1, 2, 3, 4]).some((x) => x < 0); // false

// With an asynchronous predicate, making at most 2 file checks at a time.
const anyBigFile = await Readable.from([
  'file1',
  'file2',
  'file3',
]).some(async (fileName) => {
  const stats = await stat(fileName);
  return stats.size > 1024 * 1024;
}, { concurrency: 2 });
console.log(anyBigFile); // `true` if any file in the list is bigger than 1MB
console.log('done'); // Stream has finished
copy
```

######  `readable.find(fn[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readablefindfn-options)
Added in: v17.5.0, v16.17.0
Stability: 1 - Experimental
  * `fn`
    * `data`
    * `options`
      * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) aborted if the stream is destroyed allowing to abort the `fn` call early.
  * `options`
    * `concurrency` `fn` to call on the stream at once. **Default:** `1`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns: `fn` evaluated with a truthy value, or `undefined` if no element was found.


This method is similar to `Array.prototype.find` and calls `fn` on each chunk in the stream to find a chunk with a truthy value for `fn`. Once an `fn` call's awaited return value is truthy, the stream is destroyed and the promise is fulfilled with value for which `fn` returned a truthy value. If all of the `fn` calls on the chunks return a falsy value, the promise is fulfilled with `undefined`.
```
import { Readable } from 'node:stream';
import { stat } from 'node:fs/promises';

// With a synchronous predicate.
await Readable.from([1, 2, 3, 4]).find((x) => x > 2); // 3
await Readable.from([1, 2, 3, 4]).find((x) => x > 0); // 1
await Readable.from([1, 2, 3, 4]).find((x) => x > 10); // undefined

// With an asynchronous predicate, making at most 2 file checks at a time.
const foundBigFile = await Readable.from([
  'file1',
  'file2',
  'file3',
]).find(async (fileName) => {
  const stats = await stat(fileName);
  return stats.size > 1024 * 1024;
}, { concurrency: 2 });
console.log(foundBigFile); // File name of large file, if any file in the list is bigger than 1MB
console.log('done'); // Stream has finished
copy
```

######  `readable.every(fn[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readableeveryfn-options)
Added in: v17.5.0, v16.15.0
Stability: 1 - Experimental
  * `fn`
    * `data`
    * `options`
      * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) aborted if the stream is destroyed allowing to abort the `fn` call early.
  * `options`
    * `concurrency` `fn` to call on the stream at once. **Default:** `1`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns: `true` if `fn` returned a truthy value for all of the chunks.


This method is similar to `Array.prototype.every` and calls `fn` on each chunk in the stream to check if all awaited return values are truthy value for `fn`. Once an `fn` call on a chunk awaited return value is falsy, the stream is destroyed and the promise is fulfilled with `false`. If all of the `fn` calls on the chunks return a truthy value, the promise is fulfilled with `true`.
```
import { Readable } from 'node:stream';
import { stat } from 'node:fs/promises';

// With a synchronous predicate.
await Readable.from([1, 2, 3, 4]).every((x) => x > 2); // false
await Readable.from([1, 2, 3, 4]).every((x) => x > 0); // true

// With an asynchronous predicate, making at most 2 file checks at a time.
const allBigFiles = await Readable.from([
  'file1',
  'file2',
  'file3',
]).every(async (fileName) => {
  const stats = await stat(fileName);
  return stats.size > 1024 * 1024;
}, { concurrency: 2 });
// `true` if all files in the list are bigger than 1MiB
console.log(allBigFiles);
console.log('done'); // Stream has finished
copy
```

######  `readable.flatMap(fn[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readableflatmapfn-options)
Added in: v17.5.0, v16.15.0
Stability: 1 - Experimental
  * `fn`
    * `data`
    * `options`
      * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) aborted if the stream is destroyed allowing to abort the `fn` call early.
  * `options`
    * `concurrency` `fn` to call on the stream at once. **Default:** `1`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns: [`<Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) a stream flat-mapped with the function `fn`.


This method returns a new stream by applying the given callback to each chunk of the stream and then flattening the result.
It is possible to return a stream or another iterable or async iterable from `fn` and the result streams will be merged (flattened) into the returned stream.
```
import { Readable } from 'node:stream';
import { createReadStream } from 'node:fs';

// With a synchronous mapper.
for await (const chunk of Readable.from([1, 2, 3, 4]).flatMap((x) => [x, x])) {
  console.log(chunk); // 1, 1, 2, 2, 3, 3, 4, 4
}
// With an asynchronous mapper, combine the contents of 4 files
const concatResult = Readable.from([
  './1.mjs',
  './2.mjs',
  './3.mjs',
  './4.mjs',
]).flatMap((fileName) => createReadStream(fileName));
for await (const result of concatResult) {
  // This will contain the contents (all chunks) of all 4 files
  console.log(result);
}
copy
```

######  `readable.drop(limit[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readabledroplimit-options)
Added in: v17.5.0, v16.15.0
Stability: 1 - Experimental
  * `limit`
  * `options`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns: [`<Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) a stream with `limit` chunks dropped.


This method returns a new stream with the first `limit` chunks dropped.
```
import { Readable } from 'node:stream';

await Readable.from([1, 2, 3, 4]).drop(2).toArray(); // [3, 4]
copy
```

######  `readable.take(limit[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readabletakelimit-options)
Added in: v17.5.0, v16.15.0
Stability: 1 - Experimental
  * `limit`
  * `options`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns: [`<Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) a stream with `limit` chunks taken.


This method returns a new stream with the first `limit` chunks.
```
import { Readable } from 'node:stream';

await Readable.from([1, 2, 3, 4]).take(2).toArray(); // [1, 2]
copy
```

######  `readable.reduce(fn[, initial[, options]])`[#](https://nodejs.org/docs/latest/api/stream.html#readablereducefn-initial-options)
Added in: v17.5.0, v16.15.0
Stability: 1 - Experimental
  * `fn`
    * `previous` `fn` or the `initial` value if specified or the first chunk of the stream otherwise.
    * `data`
    * `options`
      * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) aborted if the stream is destroyed allowing to abort the `fn` call early.
  * `initial`
  * `options`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns:


This method calls `fn` on each chunk of the stream in order, passing it the result from the calculation on the previous element. It returns a promise for the final value of the reduction.
If no `initial` value is supplied the first chunk of the stream is used as the initial value. If the stream is empty, the promise is rejected with a `TypeError` with the `ERR_INVALID_ARGS` code property.
```
import { Readable } from 'node:stream';
import { readdir, stat } from 'node:fs/promises';
import { join } from 'node:path';

const directoryPath = './src';
const filesInDir = await readdir(directoryPath);

const folderSize = await Readable.from(filesInDir)
  .reduce(async (totalSize, file) => {
    const { size } = await stat(join(directoryPath, file));
    return totalSize + size;
  }, 0);

console.log(folderSize);
copy
```

The reducer function iterates the stream element-by-element which means that there is no `concurrency` parameter or parallelism. To perform a `reduce` concurrently, you can extract the async function to [`readable.map`](https://nodejs.org/docs/latest/api/stream.html#readablemapfn-options) method.
```
import { Readable } from 'node:stream';
import { readdir, stat } from 'node:fs/promises';
import { join } from 'node:path';

const directoryPath = './src';
const filesInDir = await readdir(directoryPath);

const folderSize = await Readable.from(filesInDir)
  .map((file) => stat(join(directoryPath, file)), { concurrency: 2 })
  .reduce((totalSize, { size }) => totalSize + size, 0);

console.log(folderSize);
copy
```

#### Duplex and transform streams[#](https://nodejs.org/docs/latest/api/stream.html#duplex-and-transform-streams)
##### Class: `stream.Duplex`[#](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)
Added in: v0.9.4History Version | Changes
---|---
v6.8.0 | Instances of `Duplex` now return `true` when checking `instanceof stream.Writable`.
Duplex streams are streams that implement both the [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) and [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) interfaces.
Examples of `Duplex` streams include:
  * [TCP sockets](https://nodejs.org/docs/latest/api/net.html#class-netsocket)
  * [zlib streams](https://nodejs.org/docs/latest/api/zlib.html)
  * [crypto streams](https://nodejs.org/docs/latest/api/crypto.html)


######  `duplex.allowHalfOpen`[#](https://nodejs.org/docs/latest/api/stream.html#duplexallowhalfopen)
Added in: v0.9.4
  * Type:


If `false` then the stream will automatically end the writable side when the readable side ends. Set initially by the `allowHalfOpen` constructor option, which defaults to `true`.
This can be changed manually to change the half-open behavior of an existing `Duplex` stream instance, but must be changed before the `'end'` event is emitted.
##### Class: `stream.Transform`[#](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform)
Added in: v0.9.4
Transform streams are [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) streams where the output is in some way related to the input. Like all [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) streams, `Transform` streams implement both the [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) and [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) interfaces.
Examples of `Transform` streams include:
  * [zlib streams](https://nodejs.org/docs/latest/api/zlib.html)
  * [crypto streams](https://nodejs.org/docs/latest/api/crypto.html)


######  `transform.destroy([error])`[#](https://nodejs.org/docs/latest/api/stream.html#transformdestroyerror)
Added in: v8.0.0History Version | Changes
---|---
v14.0.0 | Work as a no-op on a stream that has already been destroyed.
  * `error`
  * Returns:


Destroy the stream, and optionally emit an `'error'` event. After this call, the transform stream would release any internal resources. Implementers should not override this method, but instead implement [`readable._destroy()`](https://nodejs.org/docs/latest/api/stream.html#readable_destroyerr-callback). The default implementation of `_destroy()` for `Transform` also emit `'close'` unless `emitClose` is set in false.
Once `destroy()` has been called, any further calls will be a no-op and no further errors except from `_destroy()` may be emitted as `'error'`.
#####  `stream.duplexPair([options])`[#](https://nodejs.org/docs/latest/api/stream.html#streamduplexpairoptions)
Added in: v22.6.0, v20.17.0
  * `options` [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) constructors, to set options such as buffering.
  * Returns: [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) instances.


The utility function `duplexPair` returns an Array with two items, each being a `Duplex` stream connected to the other side:
```
const [ sideA, sideB ] = duplexPair();
copy
```

Whatever is written to one stream is made readable on the other. It provides behavior analogous to a network connection, where the data written by the client becomes readable by the server, and vice-versa.
The Duplex streams are symmetrical; one or the other may be used without any difference in behavior.
####  `stream.finished(stream[, options], callback)`[#](https://nodejs.org/docs/latest/api/stream.html#streamfinishedstream-options-callback)
Added in: v10.0.0History Version | Changes
---|---
v19.5.0 | Added support for `ReadableStream` and `WritableStream`.
v15.11.0 | The `signal` option was added.
v14.0.0 | The `finished(stream, cb)` will wait for the `'close'` event before invoking the callback. The implementation tries to detect legacy streams and only apply this behavior to streams which are expected to emit `'close'`.
v14.0.0 | Emitting `'close'` before `'end'` on a `Readable` stream will cause an `ERR_STREAM_PREMATURE_CLOSE` error.
v14.0.0 | Callback will be invoked on streams which have already finished before the call to `finished(stream, cb)`.
  * `stream` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) | [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream) | [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream) A readable and/or writable stream/webstream.
  * `options`
    * `error` `false`, then a call to `emit('error', err)` is not treated as finished. **Default:** `true`.
    * `readable` `false`, the callback will be called when the stream ends even though the stream might still be readable. **Default:** `true`.
    * `writable` `false`, the callback will be called when the stream ends even though the stream might still be writable. **Default:** `true`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows aborting the wait for the stream finish. The underlying stream will  _not_ be aborted if the signal is aborted. The callback will get called with an `AbortError`. All registered listeners added by this function will also be removed.
  * `callback`
  * Returns:


A function to get notified when a stream is no longer readable, writable or has experienced an error or a premature close event.
```
const { finished } = require('node:stream');
const fs = require('node:fs');

const rs = fs.createReadStream('archive.tar');

finished(rs, (err) => {
  if (err) {
    console.error('Stream failed.', err);
  } else {
    console.log('Stream is done reading.');
  }
});

rs.resume(); // Drain the stream.
copy
```

Especially useful in error handling scenarios where a stream is destroyed prematurely (like an aborted HTTP request), and will not emit `'end'` or `'finish'`.
The `finished` API provides [promise version](https://nodejs.org/docs/latest/api/stream.html#streamfinishedstream-options).
`stream.finished()` leaves dangling event listeners (in particular `'error'`, `'end'`, `'finish'` and `'close'`) after `callback` has been invoked. The reason for this is so that unexpected `'error'` events (due to incorrect stream implementations) do not cause unexpected crashes. If this is unwanted behavior then the returned cleanup function needs to be invoked in the callback:
```
const cleanup = finished(rs, (err) => {
  cleanup();
  // ...
});
copy
```

####  `stream.pipeline(source[, ...transforms], destination, callback)`[#](https://nodejs.org/docs/latest/api/stream.html#streampipelinesource-transforms-destination-callback)
####  `stream.pipeline(streams, callback)`[#](https://nodejs.org/docs/latest/api/stream.html#streampipelinestreams-callback)
Added in: v10.0.0History Version | Changes
---|---
v19.7.0, v18.16.0 | Added support for webstreams.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v14.0.0 | The `pipeline(..., cb)` will wait for the `'close'` event before invoking the callback. The implementation tries to detect legacy streams and only apply this behavior to streams which are expected to emit `'close'`.
v13.10.0 | Add support for async generators.
  * `streams` [`<Stream[]>`](https://nodejs.org/docs/latest/api/stream.html#stream) | [`<ReadableStream[]>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream) | [`<WritableStream[]>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream) | [`<TransformStream[]>`](https://nodejs.org/docs/latest/api/webstreams.html#class-transformstream)
  * `source` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) | [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)
    * Returns:
  * `...transforms` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) | [`<TransformStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-transformstream)
    * `source`
    * Returns:
  * `destination` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) | [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream)
    * `source`
    * Returns:
  * `callback`
    * `err`
    * `val` Resolved value of `Promise` returned by `destination`.
  * Returns: [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream)

##  [`sampleRate`](https://vercel.com/docs/query#samplerate)[](https://vercel.com/docs/query#samplerate)
In prior versions of Speed Insights this was managed in the UI. This option is now managed through code with the package.
This parameter determines the percentage of events that are sent to the server. By default, all events are sent. Lowering this parameter allows for cost savings but may result in a decrease in the overall accuracy of the data being sent. For example, a `sampleRate` of `0.5` would mean that only 50% of the events will be sent to the server.
To learn more about how to configure the `sampleRate` option, see the [Sending a sample of events to Speed Insights](https://vercel.com/kb/guide/sending-sample-to-speed-insights) recipe.

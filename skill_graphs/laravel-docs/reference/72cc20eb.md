## [Events](https://laravel.com/docs/12.x/mail#events)
Laravel dispatches two events while sending mail messages. The `MessageSending` event is dispatched prior to a message being sent, while the `MessageSent` event is dispatched after a message has been sent. Remember, these events are dispatched when the mail is being _sent_ , not when it is queued. You may create [event listeners](https://laravel.com/docs/12.x/events) for these events within your application:
```


 1use Illuminate\Mail\Events\MessageSending;




 2// use Illuminate\Mail\Events\MessageSent;




 3 



 4class LogMessage




 5{




 6    /**




 7     * Handle the event.




 8     */




 9    public function handle(MessageSending $event): void




10    {




11        // ...




12    }




13}




use Illuminate\Mail\Events\MessageSending;
// use Illuminate\Mail\Events\MessageSent;

class LogMessage
{
    /**
     * Handle the event.
     */
    public function handle(MessageSending $event): void
    {
        // ...
    }
}

```

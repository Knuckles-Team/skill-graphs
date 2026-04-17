## [Service Injection](https://laravel.com/docs/12.x/blade#service-injection)
The `@inject` directive may be used to retrieve a service from the Laravel [service container](https://laravel.com/docs/12.x/container). The first argument passed to `@inject` is the name of the variable the service will be placed into, while the second argument is the class or interface name of the service you wish to resolve:
```


1@inject('metrics', 'App\Services\MetricsService')




2 



3<div>




4    Monthly Revenue: {{ $metrics->monthlyRevenue() }}.




5</div>




@inject('metrics', 'App\Services\MetricsService')

<div>
    Monthly Revenue: {{ $metrics->monthlyRevenue() }}.
</div>

```

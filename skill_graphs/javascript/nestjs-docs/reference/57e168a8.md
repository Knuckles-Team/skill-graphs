## Learn the right way!
  * 19 chapters
  * Authn & Authz
  * Official certificate
  * Deep-dive sessions

[Purchase the Authentication course](https://courses.nestjs.com/#authentication "Courses | NestJS - A node.js framework built on top of TypeScript")
####  Login route[#](https://docs.nestjs.com/recipes/passport#login-route)
With the strategy in place, we can now implement a bare-bones `/auth/login` route, and apply the built-in Guard to initiate the passport-local flow.
Open the `app.controller.ts` file and replace its contents with the following:
content_copy app.controller.ts
JS  TS
```

import { Controller, Request, Post, UseGuards } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';

@Controller()
export class AppController {
  @UseGuards(AuthGuard('local'))
  @Post('auth/login')
  async login(@Request() req) {
    return req.user;
  }
}

```
```

import { Controller, Bind, Request, Post, UseGuards } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';

@Controller()
export class AppController {
  @UseGuards(AuthGuard('local'))
  @Post('auth/login')
  @Bind(Request())
  async login(req) {
    return req.user;
  }
}

```

With `@UseGuards(AuthGuard('local'))` we are using an `AuthGuard` that `@nestjs/passport`**automatically provisioned** for us when we extended the passport-local strategy. Let's break that down. Our Passport local strategy has a default name of `'local'`. We reference that name in the `@UseGuards()` decorator to associate it with code supplied by the `passport-local` package. This is used to disambiguate which strategy to invoke in case we have multiple Passport strategies in our app (each of which may provision a strategy-specific `AuthGuard`). While we only have one such strategy so far, we'll shortly add a second, so this is needed for disambiguation.
In order to test our route we'll have our `/auth/login` route simply return the user for now. This also lets us demonstrate another Passport feature: Passport automatically creates a `user` object, based on the value we return from the `validate()` method, and assigns it to the `Request` object as `req.user`. Later, we'll replace this with code to create and return a JWT instead.
Since these are API routes, we'll test them using the commonly available `user` objects hard-coded in the `UsersService`.
```

$ # POST to /auth/login
$ curl -X POST http://localhost:3000/auth/login -d '{"username": "john", "password": "changeme"}' -H "Content-Type: application/json"
$ # result -> {"userId":1,"username":"john"}

```

While this works, passing the strategy name directly to the `AuthGuard()` introduces magic strings in the codebase. Instead, we recommend creating your own class, as shown below:
content_copy auth/local-auth.guard.ts
JS  TS
```

import { Injectable } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';

@Injectable()
export class LocalAuthGuard extends AuthGuard('local') {}

```

Now, we can update the `/auth/login` route handler and use the `LocalAuthGuard` instead:
content_copy```

@UseGuards(LocalAuthGuard)
@Post('auth/login')
async login(@Request() req) {
  return req.user;
}

```

####  Logout route[#](https://docs.nestjs.com/recipes/passport#logout-route)
To log out, we can create an additional route that invokes `req.logout()` to clear the user's session. This is a typical approach used in session-based authentication, but it does not apply to JWTs.
content_copy```

@UseGuards(LocalAuthGuard)
@Post('auth/logout')
async logout(@Request() req) {
  return req.logout();
}

```

####  JWT functionality[#](https://docs.nestjs.com/recipes/passport#jwt-functionality)
We're ready to move on to the JWT portion of our auth system. Let's review and refine our requirements:
  * Allow users to authenticate with username/password, returning a JWT for use in subsequent calls to protected API endpoints. We're well on our way to meeting this requirement. To complete it, we'll need to write the code that issues a JWT.
  * Create API routes which are protected based on the presence of a valid JWT as a bearer token


We'll need to install a couple more packages to support our JWT requirements:
```

$ npm install --save @nestjs/jwt passport-jwt
$ npm install --save-dev @types/passport-jwt

```

The `@nestjs/jwt` package (see more `passport-jwt` package is the Passport package that implements the JWT strategy and `@types/passport-jwt` provides the TypeScript type definitions.
Let's take a closer look at how a `POST /auth/login` request is handled. We've decorated the route using the built-in `AuthGuard` provided by the passport-local strategy. This means that:
  1. The route handler **will only be invoked if the user has been validated**
  2. The `req` parameter will contain a `user` property (populated by Passport during the passport-local authentication flow)


With this in mind, we can now finally generate a real JWT, and return it in this route. To keep our services cleanly modularized, we'll handle generating the JWT in the `authService`. Open the `auth.service.ts` file in the `auth` folder, and add the `login()` method, and import the `JwtService` as shown:
content_copy auth/auth.service.ts
JS  TS
```

import { Injectable } from '@nestjs/common';
import { UsersService } from '../users/users.service';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class AuthService {
  constructor(
    private usersService: UsersService,
    private jwtService: JwtService
  ) {}

  async validateUser(username: string, pass: string): Promise<any> {
    const user = await this.usersService.findOne(username);
    if (user && user.password === pass) {
      const { password, ...result } = user;
      return result;
    }
    return null;
  }

  async login(user: any) {
    const payload = { username: user.username, sub: user.userId };
    return {
      access_token: this.jwtService.sign(payload),
    };
  }
}

```
```

import { Injectable, Dependencies } from '@nestjs/common';
import { UsersService } from '../users/users.service';
import { JwtService } from '@nestjs/jwt';

@Dependencies(UsersService, JwtService)
@Injectable()
export class AuthService {
  constructor(usersService, jwtService) {
    this.usersService = usersService;
    this.jwtService = jwtService;
  }

  async validateUser(username, pass) {
    const user = await this.usersService.findOne(username);
    if (user && user.password === pass) {
      const { password, ...result } = user;
      return result;
    }
    return null;
  }

  async login(user) {
    const payload = { username: user.username, sub: user.userId };
    return {
      access_token: this.jwtService.sign(payload),
    };
  }
}

```

We're using the `@nestjs/jwt` library, which supplies a `sign()` function to generate our JWT from a subset of the `user` object properties, which we then return as a simple object with a single `access_token` property. Note: we choose a property name of `sub` to hold our `userId` value to be consistent with JWT standards. Don't forget to inject the JwtService provider into the `AuthService`.
We now need to update the `AuthModule` to import the new dependencies and configure the `JwtModule`.
First, create `constants.ts` in the `auth` folder, and add the following code:
content_copy auth/constants.ts
JS  TS
```

export const jwtConstants = {
  secret: 'DO NOT USE THIS VALUE. INSTEAD, CREATE A COMPLEX SECRET AND KEEP IT SAFE OUTSIDE OF THE SOURCE CODE.',
};

```
```

export const jwtConstants = {
  secret: 'DO NOT USE THIS VALUE. INSTEAD, CREATE A COMPLEX SECRET AND KEEP IT SAFE OUTSIDE OF THE SOURCE CODE.',
};

```

We'll use this to share our key between the JWT signing and verifying steps.
> **Warning****Do not expose this key publicly**. We have done so here to make it clear what the code is doing, but in a production system **you must protect this key** using appropriate measures such as a secrets vault, environment variable, or configuration service.
Now, open `auth.module.ts` in the `auth` folder and update it to look like this:
content_copy auth/auth.module.ts
JS  TS
```

import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { LocalStrategy } from './local.strategy';
import { UsersModule } from '../users/users.module';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';
import { jwtConstants } from './constants';

@Module({
  imports: [
    UsersModule,
    PassportModule,
    JwtModule.register({
      secret: jwtConstants.secret,
      signOptions: { expiresIn: '60s' },
    }),
  ],
  providers: [AuthService, LocalStrategy],
  exports: [AuthService],
})
export class AuthModule {}

```
```

import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { LocalStrategy } from './local.strategy';
import { UsersModule } from '../users/users.module';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';
import { jwtConstants } from './constants';

@Module({
  imports: [
    UsersModule,
    PassportModule,
    JwtModule.register({
      secret: jwtConstants.secret,
      signOptions: { expiresIn: '60s' },
    }),
  ],
  providers: [AuthService, LocalStrategy],
  exports: [AuthService],
})
export class AuthModule {}

```

We configure the `JwtModule` using `register()`, passing in a configuration object. See `JwtModule` and
Now we can update the `/auth/login` route to return a JWT.
content_copy app.controller.ts
JS  TS
```

import { Controller, Request, Post, UseGuards } from '@nestjs/common';
import { LocalAuthGuard } from './auth/local-auth.guard';
import { AuthService } from './auth/auth.service';

@Controller()
export class AppController {
  constructor(private authService: AuthService) {}

  @UseGuards(LocalAuthGuard)
  @Post('auth/login')
  async login(@Request() req) {
    return this.authService.login(req.user);
  }
}

```
```

import { Controller, Bind, Request, Post, UseGuards } from '@nestjs/common';
import { LocalAuthGuard } from './auth/local-auth.guard';
import { AuthService } from './auth/auth.service';

@Controller()
export class AppController {
  constructor(private authService: AuthService) {}

  @UseGuards(LocalAuthGuard)
  @Post('auth/login')
  @Bind(Request())
  async login(req) {
    return this.authService.login(req.user);
  }
}

```

Let's go ahead and test our routes using cURL again. You can test with any of the `user` objects hard-coded in the `UsersService`.
```

$ # POST to /auth/login
$ curl -X POST http://localhost:3000/auth/login -d '{"username": "john", "password": "changeme"}' -H "Content-Type: application/json"
$ # result -> {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}
$ # Note: above JWT truncated

```

####  Implementing Passport JWT[#](https://docs.nestjs.com/recipes/passport#implementing-passport-jwt)
We can now address our final requirement: protecting endpoints by requiring a valid JWT be present on the request. Passport can help us here too. It provides the `jwt.strategy.ts` in the `auth` folder, and add the following code:
content_copy auth/jwt.strategy.ts
JS  TS
```

import { ExtractJwt, Strategy } from 'passport-jwt';
import { PassportStrategy } from '@nestjs/passport';
import { Injectable } from '@nestjs/common';
import { jwtConstants } from './constants';

@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor() {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      ignoreExpiration: false,
      secretOrKey: jwtConstants.secret,
    });
  }

  async validate(payload: any) {
    return { userId: payload.sub, username: payload.username };
  }
}

```
```

import { ExtractJwt, Strategy } from 'passport-jwt';
import { PassportStrategy } from '@nestjs/passport';
import { Injectable } from '@nestjs/common';
import { jwtConstants } from './constants';

@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor() {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      ignoreExpiration: false,
      secretOrKey: jwtConstants.secret,
    });
  }

  async validate(payload) {
    return { userId: payload.sub, username: payload.username };
  }
}

```

With our `JwtStrategy`, we've followed the same recipe described earlier for all Passport strategies. This strategy requires some initialization, so we do that by passing in an options object in the `super()` call. You can read more about the available options
  * `jwtFromRequest`: supplies the method by which the JWT will be extracted from the `Request`. We will use the standard approach of supplying a bearer token in the Authorization header of our API requests. Other options are described
  * `ignoreExpiration`: just to be explicit, we choose the default `false` setting, which delegates the responsibility of ensuring that a JWT has not expired to the Passport module. This means that if our route is supplied with an expired JWT, the request will be denied and a `401 Unauthorized` response sent. Passport conveniently handles this automatically for us.
  * `secretOrKey`: we are using the expedient option of supplying a symmetric secret for signing the token. Other options, such as a PEM-encoded public key, may be more appropriate for production apps (see **do not expose this secret publicly**.


The `validate()` method deserves some discussion. For the jwt-strategy, Passport first verifies the JWT's signature and decodes the JSON. It then invokes our `validate()` method passing the decoded JSON as its single parameter. Based on the way JWT signing works, **we're guaranteed that we're receiving a valid token** that we have previously signed and issued to a valid user.
As a result of all this, our response to the `validate()` callback is trivial: we simply return an object containing the `userId` and `username` properties. Recall again that Passport will build a `user` object based on the return value of our `validate()` method, and attach it as a property on the `Request` object.
Additionally, you can return an array, where the first value is used to create a `user` object and the second value is used to create an `authInfo` object.
It's also worth pointing out that this approach leaves us room ('hooks' as it were) to inject other business logic into the process. For example, we could do a database lookup in our `validate()` method to extract more information about the user, resulting in a more enriched `user` object being available in our `Request`. This is also the place we may decide to do further token validation, such as looking up the `userId` in a list of revoked tokens, enabling us to perform token revocation. The model we've implemented here in our sample code is a fast, "stateless JWT" model, where each API call is immediately authorized based on the presence of a valid JWT, and a small bit of information about the requester (its `userId` and `username`) is available in our Request pipeline.
Add the new `JwtStrategy` as a provider in the `AuthModule`:
content_copy auth/auth.module.ts
JS  TS
```

import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { LocalStrategy } from './local.strategy';
import { JwtStrategy } from './jwt.strategy';
import { UsersModule } from '../users/users.module';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';
import { jwtConstants } from './constants';

@Module({
  imports: [
    UsersModule,
    PassportModule,
    JwtModule.register({
      secret: jwtConstants.secret,
      signOptions: { expiresIn: '60s' },
    }),
  ],
  providers: [AuthService, LocalStrategy, JwtStrategy],
  exports: [AuthService],
})
export class AuthModule {}

```
```

import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { LocalStrategy } from './local.strategy';
import { JwtStrategy } from './jwt.strategy';
import { UsersModule } from '../users/users.module';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';
import { jwtConstants } from './constants';

@Module({
  imports: [
    UsersModule,
    PassportModule,
    JwtModule.register({
      secret: jwtConstants.secret,
      signOptions: { expiresIn: '60s' },
    }),
  ],
  providers: [AuthService, LocalStrategy, JwtStrategy],
  exports: [AuthService],
})
export class AuthModule {}

```

By importing the same secret used when we signed the JWT, we ensure that the **verify** phase performed by Passport, and the **sign** phase performed in our AuthService, use a common secret.
Finally, we define the `JwtAuthGuard` class which extends the built-in `AuthGuard`:
content_copy auth/jwt-auth.guard.ts
JS  TS
```

import { Injectable } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';

@Injectable()
export class JwtAuthGuard extends AuthGuard('jwt') {}

```

####  Implement protected route and JWT strategy guards[#](https://docs.nestjs.com/recipes/passport#implement-protected-route-and-jwt-strategy-guards)
We can now implement our protected route and its associated Guard.
Open the `app.controller.ts` file and update it as shown below:
content_copy app.controller.ts
JS  TS
```

import { Controller, Get, Request, Post, UseGuards } from '@nestjs/common';
import { JwtAuthGuard } from './auth/jwt-auth.guard';
import { LocalAuthGuard } from './auth/local-auth.guard';
import { AuthService } from './auth/auth.service';

@Controller()
export class AppController {
  constructor(private authService: AuthService) {}

  @UseGuards(LocalAuthGuard)
  @Post('auth/login')
  async login(@Request() req) {
    return this.authService.login(req.user);
  }

  @UseGuards(JwtAuthGuard)
  @Get('profile')
  getProfile(@Request() req) {
    return req.user;
  }
}

```
```

import { Controller, Dependencies, Bind, Get, Request, Post, UseGuards } from '@nestjs/common';
import { JwtAuthGuard } from './auth/jwt-auth.guard';
import { LocalAuthGuard } from './auth/local-auth.guard';
import { AuthService } from './auth/auth.service';

@Dependencies(AuthService)
@Controller()
export class AppController {
  constructor(authService) {
    this.authService = authService;
  }

  @UseGuards(LocalAuthGuard)
  @Post('auth/login')
  @Bind(Request())
  async login(req) {
    return this.authService.login(req.user);
  }

  @UseGuards(JwtAuthGuard)
  @Get('profile')
  @Bind(Request())
  getProfile(req) {
    return req.user;
  }
}

```

Once again, we're applying the `AuthGuard` that the `@nestjs/passport` module has automatically provisioned for us when we configured the passport-jwt module. This Guard is referenced by its default name, `jwt`. When our `GET /profile` route is hit, the Guard will automatically invoke our passport-jwt custom configured strategy, validate the JWT, and assign the `user` property to the `Request` object.
Ensure the app is running, and test the routes using `cURL`.
```

$ # GET /profile
$ curl http://localhost:3000/profile
$ # result -> {"statusCode":401,"message":"Unauthorized"}

$ # POST /auth/login
$ curl -X POST http://localhost:3000/auth/login -d '{"username": "john", "password": "changeme"}' -H "Content-Type: application/json"
$ # result -> {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2Vybm... }

$ # GET /profile using access_token returned from previous step as bearer code
$ curl http://localhost:3000/profile -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2Vybm..."
$ # result -> {"userId":1,"username":"john"}

```

Note that in the `AuthModule`, we configured the JWT to have an expiration of `60 seconds`. This is probably too short an expiration, and dealing with the details of token expiration and refresh is beyond the scope of this article. However, we chose that to demonstrate an important quality of JWTs and the passport-jwt strategy. If you wait 60 seconds after authenticating before attempting a `GET /profile` request, you'll receive a `401 Unauthorized` response. This is because Passport automatically checks the JWT for its expiration time, saving you the trouble of doing so in your application.
We've now completed our JWT authentication implementation. JavaScript clients (such as Angular/React/Vue), and other JavaScript apps, can now authenticate and communicate securely with our API Server.
####  Extending guards[#](https://docs.nestjs.com/recipes/passport#extending-guards)
In most cases, using a provided `AuthGuard` class is sufficient. However, there might be use-cases when you would like to simply extend the default error handling or authentication logic. For this, you can extend the built-in class and override methods within a sub-class.
content_copy```

import {
  ExecutionContext,
  Injectable,
  UnauthorizedException,
} from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';

@Injectable()
export class JwtAuthGuard extends AuthGuard('jwt') {
  canActivate(context: ExecutionContext) {
    // Add your custom authentication logic here
    // for example, call super.logIn(request) to establish a session.
    return super.canActivate(context);
  }

  handleRequest(err, user, info) {
    // You can throw an exception based on either "info" or "err" arguments
    if (err || !user) {
      throw err || new UnauthorizedException();
    }
    return user;
  }
}

```

In addition to extending the default error handling and authentication logic, we can allow authentication to go through a chain of strategies. The first strategy to succeed, redirect, or error will halt the chain. Authentication failures will proceed through each strategy in series, ultimately failing if all strategies fail.
content_copy```

export class JwtAuthGuard extends AuthGuard(['strategy_jwt_1', 'strategy_jwt_2', '...']) { ... }

```

####  Enable authentication globally[#](https://docs.nestjs.com/recipes/passport#enable-authentication-globally)
If the vast majority of your endpoints should be protected by default, you can register the authentication guard as a [global guard](https://docs.nestjs.com/guards#binding-guards) and instead of using `@UseGuards()` decorator on top of each controller, you could simply flag which routes should be public.
First, register the `JwtAuthGuard` as a global guard using the following construction (in any module):
content_copy```

providers: [
  {
    provide: APP_GUARD,
    useClass: JwtAuthGuard,
  },
],

```

With this in place, Nest will automatically bind `JwtAuthGuard` to all endpoints.
Now we must provide a mechanism for declaring routes as public. For this, we can create a custom decorator using the `SetMetadata` decorator factory function.
content_copy```

import { SetMetadata } from '@nestjs/common';

export const IS_PUBLIC_KEY = 'isPublic';
export const Public = () => SetMetadata(IS_PUBLIC_KEY, true);

```

In the file above, we exported two constants. One being our metadata key named `IS_PUBLIC_KEY`, and the other being our new decorator itself that we’re going to call `Public` (you can alternatively name it `SkipAuth` or `AllowAnon`, whatever fits your project).
Now that we have a custom `@Public()` decorator, we can use it to decorate any method, as follows:
content_copy```

@Public()
@Get()
findAll() {
  return [];
}

```

Lastly, we need the `JwtAuthGuard` to return `true` when the `"isPublic"` metadata is found. For this, we'll use the `Reflector` class (read more [here](https://docs.nestjs.com/guards#putting-it-all-together)).
content_copy```

@Injectable()
export class JwtAuthGuard extends AuthGuard('jwt') {
  constructor(private reflector: Reflector) {
    super();
  }

  canActivate(context: ExecutionContext) {
    const isPublic = this.reflector.getAllAndOverride<boolean>(IS_PUBLIC_KEY, [
      context.getHandler(),
      context.getClass(),
    ]);
    if (isPublic) {
      return true;
    }
    return super.canActivate(context);
  }
}

```

####  Request-scoped strategies[#](https://docs.nestjs.com/recipes/passport#request-scoped-strategies)
The passport API is based on registering strategies to the global instance of the library. Therefore strategies are not designed to have request-dependent options or to be dynamically instantiated per request (read more about the [request-scoped](https://docs.nestjs.com/fundamentals/injection-scopes) providers). When you configure your strategy to be request-scoped, Nest will never instantiate it since it's not tied to any specific route. There is no physical way to determine which "request-scoped" strategies should be executed per request.
However, there are ways to dynamically resolve request-scoped providers within the strategy. For this, we leverage the [module reference](https://docs.nestjs.com/fundamentals/module-ref) feature.
First, open the `local.strategy.ts` file and inject the `ModuleRef` in the normal way:
content_copy```

constructor(private moduleRef: ModuleRef) {
  super({
    passReqToCallback: true,
  });
}

```

> **Hint** The `ModuleRef` class is imported from the `@nestjs/core` package.
Be sure to set the `passReqToCallback` configuration property to `true`, as shown above.
In the next step, the request instance will be used to obtain the current context identifier, instead of generating a new one (read more about request context [here](https://docs.nestjs.com/fundamentals/module-ref#getting-current-sub-tree)).
Now, inside the `validate()` method of the `LocalStrategy` class, use the `getByRequest()` method of the `ContextIdFactory` class to create a context id based on the request object, and pass this to the `resolve()` call:
content_copy```

async validate(
  request: Request,
  username: string,
  password: string,
) {
  const contextId = ContextIdFactory.getByRequest(request);
  // "AuthService" is a request-scoped provider
  const authService = await this.moduleRef.resolve(AuthService, contextId);
  ...
}

```

In the example above, the `resolve()` method will asynchronously return the request-scoped instance of the `AuthService` provider (we assumed that `AuthService` is marked as a request-scoped provider).
####  Customize Passport[#](https://docs.nestjs.com/recipes/passport#customize-passport)
Any standard Passport customization options can be passed the same way, using the `register()` method. The available options depend on the strategy being implemented. For example:
content_copy```

PassportModule.register({ session: true });

```

You can also pass strategies an options object in their constructors to configure them. For the local strategy you can pass e.g.:
content_copy```

constructor(private authService: AuthService) {
  super({
    usernameField: 'email',
    passwordField: 'password',
  });
}

```

Take a look at the official
####  Named strategies[#](https://docs.nestjs.com/recipes/passport#named-strategies)
When implementing a strategy, you can provide a name for it by passing a second argument to the `PassportStrategy` function. If you don't do this, each strategy will have a default name (e.g., 'jwt' for jwt-strategy):
content_copy```

export class JwtStrategy extends PassportStrategy(Strategy, 'myjwt')

```

Then, you refer to this via a decorator like `@UseGuards(AuthGuard('myjwt'))`.
####  GraphQL[#](https://docs.nestjs.com/recipes/passport#graphql)
In order to use an AuthGuard with [GraphQL](https://docs.nestjs.com/graphql/quick-start), extend the built-in `AuthGuard` class and override the `getRequest()` method.
content_copy```

@Injectable()
export class GqlAuthGuard extends AuthGuard('jwt') {
  getRequest(context: ExecutionContext) {
    const ctx = GqlExecutionContext.create(context);
    return ctx.getContext().req;
  }
}

```

To get the current authenticated user in your graphql resolver, you can define a `@CurrentUser()` decorator:
content_copy```

import { createParamDecorator, ExecutionContext } from '@nestjs/common';
import { GqlExecutionContext } from '@nestjs/graphql';

export const CurrentUser = createParamDecorator(
  (data: unknown, context: ExecutionContext) => {
    const ctx = GqlExecutionContext.create(context);
    return ctx.getContext().req.user;
  },
);

```

To use above decorator in your resolver, be sure to include it as a parameter of your query or mutation:
content_copy```

@Query(() => User)
@UseGuards(GqlAuthGuard)
whoAmI(@CurrentUser() user: User) {
  return this.usersService.findById(user.id);
}

```

For the passport-local strategy, you'll also need to add the GraphQL context's arguments to the request body so Passport can access them for validation. Otherwise, you'll get an Unauthorized error.
content_copy```

@Injectable()
export class GqlLocalAuthGuard extends AuthGuard('local') {
  getRequest(context: ExecutionContext) {
    const gqlExecutionContext = GqlExecutionContext.create(context);
    const gqlContext = gqlExecutionContext.getContext();
    const gqlArgs = gqlExecutionContext.getArgs();

    gqlContext.req.body = { ...gqlContext.req.body, ...gqlArgs };
    return gqlContext.req;
  }
}

```

### Support us
Nest is an MIT-licensed open source project. It can grow thanks to the support of these awesome people. If you'd like to join them, please read more [here](https://docs.nestjs.com/support).
#### Principal Sponsors
#### Sponsors / Partners
### Join our Newsletter
Subscribe to stay up to date with the latest Nest updates, features, and videos!
Copyright © 2017-2026 MIT by
Official NestJS Consulting

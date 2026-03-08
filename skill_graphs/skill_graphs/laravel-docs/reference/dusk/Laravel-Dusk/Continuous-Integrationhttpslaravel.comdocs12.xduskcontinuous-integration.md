## [Continuous Integration](https://laravel.com/docs/12.x/dusk#continuous-integration)
Most Dusk continuous integration configurations expect your Laravel application to be served using the built-in PHP development server on port 8000. Therefore, before continuing, you should ensure that your continuous integration environment has an `APP_URL` environment variable value of `http://127.0.0.1:8000`.
### [Heroku CI](https://laravel.com/docs/12.x/dusk#running-tests-on-heroku-ci)
To run Dusk tests on `app.json` file:
```


 1{




 2  "environments": {




 3    "test": {




 4      "buildpacks": [




 5        { "url": "heroku/php" },




 6        { "url": "https://github.com/heroku/heroku-buildpack-chrome-for-testing" }




 7      ],




 8      "scripts": {




 9        "test-setup": "cp .env.testing .env",




10        "test": "nohup bash -c './vendor/laravel/dusk/bin/chromedriver-linux --port=9515 > /dev/null 2>&1 &' && nohup bash -c 'php artisan serve --no-reload > /dev/null 2>&1 &' && php artisan dusk"




11      }




12    }




13  }




14}




{
  "environments": {
    "test": {
      "buildpacks": [
        { "url": "heroku/php" },
        { "url": "https://github.com/heroku/heroku-buildpack-chrome-for-testing" }
      ],
      "scripts": {
        "test-setup": "cp .env.testing .env",
        "test": "nohup bash -c './vendor/laravel/dusk/bin/chromedriver-linux --port=9515 > /dev/null 2>&1 &' && nohup bash -c 'php artisan serve --no-reload > /dev/null 2>&1 &' && php artisan dusk"
      }
    }
  }
}

```

### [Travis CI](https://laravel.com/docs/12.x/dusk#running-tests-on-travis-ci)
To run your Dusk tests on `.travis.yml` configuration. Since Travis CI is not a graphical environment, we will need to take some extra steps in order to launch a Chrome browser. In addition, we will use `php artisan serve` to launch PHP's built-in web server:
```


 1language: php




 2 



 3php:




 4  - 8.2




 5 



 6addons:




 7  chrome: stable




 8 



 9install:




10  - cp .env.testing .env




11  - travis_retry composer install --no-interaction --prefer-dist




12  - php artisan key:generate




13  - php artisan dusk:chrome-driver




14 



15before_script:




16  - google-chrome-stable --headless --disable-gpu --remote-debugging-port=9222 http://localhost &




17  - php artisan serve --no-reload &




18 



19script:




20  - php artisan dusk




language: php

php:
  - 8.2

addons:
  chrome: stable

install:
  - cp .env.testing .env
  - travis_retry composer install --no-interaction --prefer-dist
  - php artisan key:generate
  - php artisan dusk:chrome-driver

before_script:
  - google-chrome-stable --headless --disable-gpu --remote-debugging-port=9222 http://localhost &
  - php artisan serve --no-reload &

script:
  - php artisan dusk

```

### [GitHub Actions](https://laravel.com/docs/12.x/dusk#running-tests-on-github-actions)
If you are using `php artisan serve` command to launch PHP's built-in web server:
```


 1name: CI




 2on: [push]




 3jobs:




 4 



 5  dusk-php:




 6    runs-on: ubuntu-latest




 7    env:




 8      APP_URL: "http://127.0.0.1:8000"




 9      DB_USERNAME: root




10      DB_PASSWORD: root




11      MAIL_MAILER: log




12    steps:




13      - uses: actions/checkout@v5




14      - name: Prepare The Environment




15        run: cp .env.example .env




16      - name: Create Database




17        run: |




18          sudo systemctl start mysql




19          mysql --user="root" --password="root" -e "CREATE DATABASE \`my-database\` character set UTF8mb4 collate utf8mb4_bin;"




20      - name: Install Composer Dependencies




21        run: composer install --no-progress --prefer-dist --optimize-autoloader




22      - name: Generate Application Key




23        run: php artisan key:generate




24      - name: Upgrade Chrome Driver




25        run: php artisan dusk:chrome-driver --detect




26      - name: Start Chrome Driver




27        run: ./vendor/laravel/dusk/bin/chromedriver-linux --port=9515 &




28      - name: Run Laravel Server




29        run: php artisan serve --no-reload &




30      - name: Run Dusk Tests




31        run: php artisan dusk




32      - name: Upload Screenshots




33        if: failure()




34        uses: actions/upload-artifact@v4




35        with:




36          name: screenshots




37          path: tests/Browser/screenshots




38      - name: Upload Console Logs




39        if: failure()




40        uses: actions/upload-artifact@v4




41        with:




42          name: console




43          path: tests/Browser/console




name: CI
on: [push]
jobs:

  dusk-php:
    runs-on: ubuntu-latest
    env:
      APP_URL: "http://127.0.0.1:8000"
      DB_USERNAME: root
      DB_PASSWORD: root
      MAIL_MAILER: log
    steps:
      - uses: actions/checkout@v5
      - name: Prepare The Environment
        run: cp .env.example .env
      - name: Create Database
        run: |
          sudo systemctl start mysql
          mysql --user="root" --password="root" -e "CREATE DATABASE \`my-database\` character set UTF8mb4 collate utf8mb4_bin;"
      - name: Install Composer Dependencies
        run: composer install --no-progress --prefer-dist --optimize-autoloader
      - name: Generate Application Key
        run: php artisan key:generate
      - name: Upgrade Chrome Driver
        run: php artisan dusk:chrome-driver --detect
      - name: Start Chrome Driver
        run: ./vendor/laravel/dusk/bin/chromedriver-linux --port=9515 &
      - name: Run Laravel Server
        run: php artisan serve --no-reload &
      - name: Run Dusk Tests
        run: php artisan dusk
      - name: Upload Screenshots
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: screenshots
          path: tests/Browser/screenshots
      - name: Upload Console Logs
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: console
          path: tests/Browser/console

```

### [Chipper CI](https://laravel.com/docs/12.x/dusk#running-tests-on-chipper-ci)
If you are using
```


 1# file .chipperci.yml




 2version: 1




 3 



 4environment:




 5  php: 8.2




 6  node: 16




 7 



 8# Include Chrome in the build environment




 9services:




10  - dusk




11 



12# Build all commits




13on:




14   push:




15      branches: .*




16 



17pipeline:




18  - name: Setup




19    cmd: |




20      cp -v .env.example .env




21      composer install --no-interaction --prefer-dist --optimize-autoloader




22      php artisan key:generate




23 



24      # Create a dusk env file, ensuring APP_URL uses BUILD_HOST




25      cp -v .env .env.dusk.ci




26      sed -i "s@APP_URL=.*@APP_URL=http://$BUILD_HOST:8000@g" .env.dusk.ci




27 



28  - name: Compile Assets




29    cmd: |




30      npm ci --no-audit




31      npm run build




32 



33  - name: Browser Tests




34    cmd: |




35      php -S [::0]:8000 -t public 2>server.log &




36      sleep 2




37      php artisan dusk:chrome-driver $CHROME_DRIVER




38      php artisan dusk --env=ci




# file .chipperci.yml
version: 1

environment:
  php: 8.2
  node: 16

# Include Chrome in the build environment
services:
  - dusk

# Build all commits
on:
   push:
      branches: .*

pipeline:
  - name: Setup
    cmd: |
      cp -v .env.example .env
      composer install --no-interaction --prefer-dist --optimize-autoloader
      php artisan key:generate

      # Create a dusk env file, ensuring APP_URL uses BUILD_HOST
      cp -v .env .env.dusk.ci
      sed -i "s@APP_URL=.*@APP_URL=http://$BUILD_HOST:8000@g" .env.dusk.ci

  - name: Compile Assets
    cmd: |
      npm ci --no-audit
      npm run build

  - name: Browser Tests
    cmd: |
      php -S [::0]:8000 -t public 2>server.log &
      sleep 2
      php artisan dusk:chrome-driver $CHROME_DRIVER
      php artisan dusk --env=ci

```

To learn more about running Dusk tests on Chipper CI, including how to use databases, consult the
Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/dusk#introduction)
  * [ Installation ](https://laravel.com/docs/12.x/dusk#installation)
    * [ Managing ChromeDriver Installations ](https://laravel.com/docs/12.x/dusk#managing-chromedriver-installations)
    * [ Using Other Browsers ](https://laravel.com/docs/12.x/dusk#using-other-browsers)
  * [ Getting Started ](https://laravel.com/docs/12.x/dusk#getting-started)
    * [ Generating Tests ](https://laravel.com/docs/12.x/dusk#generating-tests)
    * [ Resetting the Database After Each Test ](https://laravel.com/docs/12.x/dusk#resetting-the-database-after-each-test)
    * [ Running Tests ](https://laravel.com/docs/12.x/dusk#running-tests)
    * [ Environment Handling ](https://laravel.com/docs/12.x/dusk#environment-handling)
  * [ Browser Basics ](https://laravel.com/docs/12.x/dusk#browser-basics)
    * [ Creating Browsers ](https://laravel.com/docs/12.x/dusk#creating-browsers)
    * [ Navigation ](https://laravel.com/docs/12.x/dusk#navigation)
    * [ Resizing Browser Windows ](https://laravel.com/docs/12.x/dusk#resizing-browser-windows)
    * [ Browser Macros ](https://laravel.com/docs/12.x/dusk#browser-macros)
    * [ Authentication ](https://laravel.com/docs/12.x/dusk#authentication)
    * [ Cookies ](https://laravel.com/docs/12.x/dusk#cookies)
    * [ Executing JavaScript ](https://laravel.com/docs/12.x/dusk#executing-javascript)
    * [ Taking a Screenshot ](https://laravel.com/docs/12.x/dusk#taking-a-screenshot)
    * [ Storing Console Output to Disk ](https://laravel.com/docs/12.x/dusk#storing-console-output-to-disk)
    * [ Storing Page Source to Disk ](https://laravel.com/docs/12.x/dusk#storing-page-source-to-disk)
  * [ Interacting With Elements ](https://laravel.com/docs/12.x/dusk#interacting-with-elements)
    * [ Dusk Selectors ](https://laravel.com/docs/12.x/dusk#dusk-selectors)
    * [ Text, Values, and Attributes ](https://laravel.com/docs/12.x/dusk#text-values-and-attributes)
    * [ Interacting With Forms ](https://laravel.com/docs/12.x/dusk#interacting-with-forms)
    * [ Attaching Files ](https://laravel.com/docs/12.x/dusk#attaching-files)
    * [ Pressing Buttons ](https://laravel.com/docs/12.x/dusk#pressing-buttons)
    * [ Clicking Links ](https://laravel.com/docs/12.x/dusk#clicking-links)
    * [ Using the Keyboard ](https://laravel.com/docs/12.x/dusk#using-the-keyboard)
    * [ Using the Mouse ](https://laravel.com/docs/12.x/dusk#using-the-mouse)
    * [ JavaScript Dialogs ](https://laravel.com/docs/12.x/dusk#javascript-dialogs)
    * [ Interacting With Inline Frames ](https://laravel.com/docs/12.x/dusk#interacting-with-iframes)
    * [ Scoping Selectors ](https://laravel.com/docs/12.x/dusk#scoping-selectors)
    * [ Waiting for Elements ](https://laravel.com/docs/12.x/dusk#waiting-for-elements)
    * [ Scrolling an Element Into View ](https://laravel.com/docs/12.x/dusk#scrolling-an-element-into-view)
  * [ Available Assertions ](https://laravel.com/docs/12.x/dusk#available-assertions)
  * [ Pages ](https://laravel.com/docs/12.x/dusk#pages)
    * [ Generating Pages ](https://laravel.com/docs/12.x/dusk#generating-pages)
    * [ Configuring Pages ](https://laravel.com/docs/12.x/dusk#configuring-pages)
    * [ Navigating to Pages ](https://laravel.com/docs/12.x/dusk#navigating-to-pages)
    * [ Shorthand Selectors ](https://laravel.com/docs/12.x/dusk#shorthand-selectors)
    * [ Page Methods ](https://laravel.com/docs/12.x/dusk#page-methods)
  * [ Components ](https://laravel.com/docs/12.x/dusk#components)
    * [ Generating Components ](https://laravel.com/docs/12.x/dusk#generating-components)
    * [ Using Components ](https://laravel.com/docs/12.x/dusk#using-components)
  * [ Continuous Integration ](https://laravel.com/docs/12.x/dusk#continuous-integration)
    * [ Heroku CI ](https://laravel.com/docs/12.x/dusk#running-tests-on-heroku-ci)
    * [ Travis CI ](https://laravel.com/docs/12.x/dusk#running-tests-on-travis-ci)
    * [ GitHub Actions ](https://laravel.com/docs/12.x/dusk#running-tests-on-github-actions)
    * [ Chipper CI ](https://laravel.com/docs/12.x/dusk#running-tests-on-chipper-ci)


[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [ More Partners ](https://partners.laravel.com)

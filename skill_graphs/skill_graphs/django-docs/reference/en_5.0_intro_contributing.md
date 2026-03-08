This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/intro/contributing/#main-content)
[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.
Menu Main navigation
  * [Overview](https://www.djangoproject.com/start/overview/)
  * [Download](https://www.djangoproject.com/download/)
  * [Documentation](https://docs.djangoproject.com/)
  * [News](https://www.djangoproject.com/weblog/)
  * [Issues](https://code.djangoproject.com/)
  * [Community](https://www.djangoproject.com/community/)
  * [Foundation](https://www.djangoproject.com/foundation/)
  * [♥ Donate](https://www.djangoproject.com/fundraising/)


Search Submit
Toggle theme (current theme: auto)
Toggle theme (current theme: light)
Toggle theme (current theme: dark)
Toggle Light / Dark / Auto color theme
[Documentation](https://docs.djangoproject.com/en/5.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/5.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/intro/contributing/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/intro/contributing/)
  * [pl](https://docs.djangoproject.com/pl/5.0/intro/contributing/)
  * [ko](https://docs.djangoproject.com/ko/5.0/intro/contributing/)
  * [ja](https://docs.djangoproject.com/ja/5.0/intro/contributing/)
  * [it](https://docs.djangoproject.com/it/5.0/intro/contributing/)
  * [id](https://docs.djangoproject.com/id/5.0/intro/contributing/)
  * [fr](https://docs.djangoproject.com/fr/5.0/intro/contributing/)
  * [es](https://docs.djangoproject.com/es/5.0/intro/contributing/)
  * [el](https://docs.djangoproject.com/el/5.0/intro/contributing/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/intro/contributing/)
  * [6.0](https://docs.djangoproject.com/en/6.0/intro/contributing/)
  * [5.2](https://docs.djangoproject.com/en/5.2/intro/contributing/)
  * [5.1](https://docs.djangoproject.com/en/5.1/intro/contributing/)
  * [4.2](https://docs.djangoproject.com/en/4.2/intro/contributing/)
  * [4.1](https://docs.djangoproject.com/en/4.1/intro/contributing/)
  * [4.0](https://docs.djangoproject.com/en/4.0/intro/contributing/)
  * [3.2](https://docs.djangoproject.com/en/3.2/intro/contributing/)
  * [3.1](https://docs.djangoproject.com/en/3.1/intro/contributing/)
  * [3.0](https://docs.djangoproject.com/en/3.0/intro/contributing/)
  * [2.2](https://docs.djangoproject.com/en/2.2/intro/contributing/)
  * [2.1](https://docs.djangoproject.com/en/2.1/intro/contributing/)
  * [2.0](https://docs.djangoproject.com/en/2.0/intro/contributing/)
  * [1.11](https://docs.djangoproject.com/en/1.11/intro/contributing/)
  * [1.10](https://docs.djangoproject.com/en/1.10/intro/contributing/)
  * [1.8](https://docs.djangoproject.com/en/1.8/intro/contributing/)


  * [](https://docs.djangoproject.com/en/5.0/intro/contributing/#top)


# Writing your first contribution for Django[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#writing-your-first-contribution-for-django "Link to this heading")
## Introduction[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#introduction "Link to this heading")
Interested in giving back to the community a little? Maybe you’ve found a bug in Django that you’d like to see fixed, or maybe there’s a small feature you want added.
Contributing back to Django itself is the best way to see your own concerns addressed. This may seem daunting at first, but it’s a well-traveled path with documentation, tooling, and a community to support you. We’ll walk you through the entire process, so you can learn by example.
### Who’s this tutorial for?[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#who-s-this-tutorial-for "Link to this heading")
See also
If you are looking for a reference on the details of making code contributions, see the [Writing code](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/) documentation.
For this tutorial, we expect that you have at least a basic understanding of how Django works. This means you should be comfortable going through the existing tutorials on [writing your first Django app](https://docs.djangoproject.com/en/5.0/intro/tutorial01/). In addition, you should have a good understanding of Python itself. But if you don’t,
Those of you who are unfamiliar with version control systems and Trac will find that this tutorial and its links include just enough information to get started. However, you’ll probably want to read some more about these different tools if you plan on contributing to Django regularly.
For the most part though, this tutorial tries to explain as much as possible, so that it can be of use to the widest audience.
Where to get help:
If you’re having trouble going through this tutorial, please post a message on the [Django Forum](https://forum.djangoproject.com/), [django-developers](https://docs.djangoproject.com/en/5.0/internals/mailing-lists/#django-developers-mailing-list), or drop by
### What does this tutorial cover?[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#what-does-this-tutorial-cover "Link to this heading")
We’ll be walking you through contributing to Django for the first time. By the end of this tutorial, you should have a basic understanding of both the tools and the processes involved. Specifically, we’ll be covering the following:
  * Installing Git.
  * Downloading a copy of Django’s development version.
  * Running Django’s test suite.
  * Writing a test for your changes.
  * Writing the code for your changes.
  * Testing your changes.
  * Submitting a pull request.
  * Where to look for more information.


Once you’re done with the tutorial, you can look through the rest of [Django’s documentation on contributing](https://docs.djangoproject.com/en/5.0/internals/contributing/). It contains lots of great information and is a must read for anyone who’d like to become a regular contributor to Django. If you’ve got questions, it’s probably got the answers.
Python 3 required!
The current version of Django doesn’t support Python 2.7. Get Python 3 at
For Windows users
See [Install Python](https://docs.djangoproject.com/en/5.0/howto/windows/#install-python-windows) on Windows docs for additional guidance.
## Code of Conduct[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#code-of-conduct "Link to this heading")
As a contributor, you can help us keep the Django community open and inclusive. Please read and follow our [Code of Conduct](https://www.djangoproject.com/conduct/).
## Installing Git[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#installing-git "Link to this heading")
For this tutorial, you’ll need Git installed to download the current development version of Django and to generate a branch for the changes you make.
To check whether or not you have Git installed, enter `git` into the command line. If you get messages saying that this command could not be found, you’ll have to download and install it, see
If you’re not that familiar with Git, you can always find out more about its commands (once it’s installed) by typing `git help` into the command line.
## Getting a copy of Django’s development version[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#getting-a-copy-of-django-s-development-version "Link to this heading")
The first step to contributing to Django is to get a copy of the source code. First, `cd` command to navigate to the directory where you’ll want your local copy of Django to live.
Download the Django source code repository using the following command:
/ 
```
$ git clone https://github.com/YourGitHubName/django.git

```

```
...\> git clone https://github.com/YourGitHubName/django.git

```

Low bandwidth connection?
You can add the `--depth 1` argument to `git clone` to skip downloading all of Django’s commit history, which reduces data transfer from ~250 MB to ~70 MB.
Now that you have a local copy of Django, you can install it just like you would install any package using `pip`. The most convenient way to do so is by using a _virtual environment_ , which is a feature built into Python that allows you to keep a separate directory of installed packages for each of your projects so that they don’t interfere with each other.
It’s a good idea to keep all your virtual environments in one place, for example in `.virtualenvs/` in your home directory.
Create a new virtual environment by running:
/ 
```
$ python3 -m venv ~/.virtualenvs/djangodev

```

```
...\> py -m venv %HOMEPATH%\.virtualenvs\djangodev

```

The path is where the new environment will be saved on your computer.
The final step in setting up your virtual environment is to activate it:
```
$ source ~/.virtualenvs/djangodev/bin/activate

```

If the `source` command is not available, you can try using a dot instead:
```
$ . ~/.virtualenvs/djangodev/bin/activate

```

You have to activate the virtual environment whenever you open a new terminal window.
For Windows users
To activate your virtual environment on Windows, run:
```
...\> %HOMEPATH%\.virtualenvs\djangodev\Scripts\activate.bat

```

The name of the currently activated virtual environment is displayed on the command line to help you keep track of which one you are using. Anything you install through `pip` while this name is displayed will be installed in that virtual environment, isolated from other environments and system-wide packages.
Go ahead and install the previously cloned copy of Django:
/ 
```
$ python -m pip install -e /path/to/your/local/clone/django/

```

```
...\> py -m pip install -e \path\to\your\local\clone\django\

```

The installed version of Django is now pointing at your local copy by installing in editable mode. You will immediately see any changes you make to it, which is of great help when writing your first contribution.
### Creating projects with a local copy of Django[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#creating-projects-with-a-local-copy-of-django "Link to this heading")
It may be helpful to test your local changes with a Django project. First you have to create a new virtual environment, [install the previously cloned local copy of Django in editable mode](https://docs.djangoproject.com/en/5.0/intro/contributing/#intro-contributing-install-local-copy), and create a new Django project outside of your local copy of Django. You will immediately see any changes you make to Django in your new project, which is of great help when writing your first contribution, especially if testing any changes to the UI.
You can follow the [tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/) for help in creating a Django project.
## Running Django’s test suite for the first time[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#running-django-s-test-suite-for-the-first-time "Link to this heading")
When contributing to Django it’s very important that your code changes don’t introduce bugs into other areas of Django. One way to check that Django still works after you make your changes is by running Django’s test suite. If all the tests still pass, then you can be reasonably sure that your changes work and haven’t broken other parts of Django. If you’ve never run Django’s test suite before, it’s a good idea to run it once beforehand to get familiar with its output.
Before running the test suite, enter the Django `tests/` directory using the `cd tests` command, and install test dependencies by running:
/ 
```
$ python -m pip install -r requirements/py3.txt

```

```
...\> py -m pip install -r requirements\py3.txt

```

If you encounter an error during the installation, your system might be missing a dependency for one or more of the Python packages. Consult the failing package’s documentation or search the web with the error message that you encounter.
Now we are ready to run the test suite. If you’re using GNU/Linux, macOS, or some other flavor of Unix, run:
/ 
```
$ ./runtests.py

```

```
...\> runtests.py

```

Now sit back and relax. Django’s entire test suite has thousands of tests, and it takes at least a few minutes to run, depending on the speed of your computer.
While Django’s test suite is running, you’ll see a stream of characters representing the status of each test as it completes. `E` indicates that an error was raised during a test, and `F` indicates that a test’s assertions failed. Both of these are considered to be test failures. Meanwhile, `x` and `s` indicated expected failures and skipped tests, respectively. Dots indicate passing tests.
Skipped tests are typically due to missing external libraries required to run the test; see [Running all the tests](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/unit-tests/#running-unit-tests-dependencies) for a list of dependencies and be sure to install any for tests related to the changes you are making (we won’t need any for this tutorial). Some tests are specific to a particular database backend and will be skipped if not testing with that backend. SQLite is the database backend for the default settings. To run the tests using a different backend, see [Using another settings module](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/unit-tests/#running-unit-tests-settings).
Once the tests complete, you should be greeted with a message informing you whether the test suite passed or failed. Since you haven’t yet made any changes to Django’s code, the entire test suite **should** pass. If you get failures or errors make sure you’ve followed all of the previous steps properly. See [Running the unit tests](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/unit-tests/#running-unit-tests) for more information.
Note that the latest Django “main” branch may not always be stable. When developing against “main”, you can check
Note
For this tutorial and the ticket we’re working on, testing against SQLite is sufficient, however, it’s possible (and sometimes necessary) to [run the tests using a different database](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/unit-tests/#running-unit-tests-settings). When making UI changes, you will need to [run the Selenium tests](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/unit-tests/#running-selenium-tests).
## Working on a feature[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#working-on-a-feature "Link to this heading")
For this tutorial, we’ll work on a “fake ticket” as a case study. Here are the imaginary details:
Ticket #99999 – Allow making toast
Django should provide a function `django.shortcuts.make_toast()` that returns `'toast'`.
We’ll now implement this feature and associated tests.
## Creating a branch[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#creating-a-branch "Link to this heading")
Before making any changes, create a new branch for the ticket:
/ 
```
$ git checkout -b ticket_99999

```

```
...\> git checkout -b ticket_99999

```

You can choose any name that you want for the branch, “ticket_99999” is an example. All changes made in this branch will be specific to the ticket and won’t affect the main copy of the code that we cloned earlier.
## Writing some tests for your ticket[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#writing-some-tests-for-your-ticket "Link to this heading")
In most cases, for a contribution to be accepted into Django it has to include tests. For bug fix contributions, this means writing a regression test to ensure that the bug is never reintroduced into Django later on. A regression test should be written in such a way that it will fail while the bug still exists and pass once the bug has been fixed. For contributions containing new features, you’ll need to include tests which ensure that the new features are working correctly. They too should fail when the new feature is not present, and then pass once it has been implemented.
A good way to do this is to write your new tests first, before making any changes to the code. This style of development is called
Now for our hands-on example.
### Writing a test for ticket #99999[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#writing-a-test-for-ticket-99999 "Link to this heading")
In order to resolve this ticket, we’ll add a `make_toast()` function to the `django.shortcuts` module. First we are going to write a test that tries to use the function and check that its output looks correct.
Navigate to Django’s `tests/shortcuts/` folder and create a new file `test_make_toast.py`. Add the following code:
```
from django.shortcuts import make_toast
from django.test import SimpleTestCase


class MakeToastTests(SimpleTestCase):
    def test_make_toast(self):
        self.assertEqual(make_toast(), "toast")

```

This test checks that the `make_toast()` returns `'toast'`.
But this testing thing looks kinda hard…
If you’ve never had to deal with tests before, they can look a little hard to write at first glance. Fortunately, testing is a _very_ big subject in computer programming, so there’s lots of information out there:
  * A good first look at writing tests for Django can be found in the documentation on [Writing and running tests](https://docs.djangoproject.com/en/5.0/topics/testing/overview/).
  * Dive Into Python (a free online book for beginning Python developers) includes a great
  * After reading those, if you want something a little meatier to sink your teeth into, there’s always the Python


### Running your new test[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#running-your-new-test "Link to this heading")
Since we haven’t made any modifications to `django.shortcuts` yet, our test should fail. Let’s run all the tests in the `shortcuts` folder to make sure that’s really what happens. `cd` to the Django `tests/` directory and run:
/ 
```
$ ./runtests.py shortcuts

```

```
...\> runtests.py shortcuts

```

If the tests ran correctly, you should see one failure corresponding to the test method we added, with this error:
```
ImportError: cannot import name 'make_toast' from 'django.shortcuts'

```

If all of the tests passed, then you’ll want to make sure that you added the new test shown above to the appropriate folder and file name.
## Writing the code for your ticket[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#writing-the-code-for-your-ticket "Link to this heading")
Next we’ll be adding the `make_toast()` function.
Navigate to the `django/` folder and open the `shortcuts.py` file. At the bottom, add:
```
def make_toast():
    return "toast"

```

Now we need to make sure that the test we wrote earlier passes, so we can see whether the code we added is working correctly. Again, navigate to the Django `tests/` directory and run:
/ 
```
$ ./runtests.py shortcuts

```

```
...\> runtests.py shortcuts

```

Everything should pass. If it doesn’t, make sure you correctly added the function to the correct file.
## Running Django’s test suite for the second time[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#running-django-s-test-suite-for-the-second-time "Link to this heading")
Once you’ve verified that your changes and test are working correctly, it’s a good idea to run the entire Django test suite to verify that your change hasn’t introduced any bugs into other areas of Django. While successfully passing the entire test suite doesn’t guarantee your code is bug free, it does help identify many bugs and regressions that might otherwise go unnoticed.
To run the entire Django test suite, `cd` into the Django `tests/` directory and run:
/ 
```
$ ./runtests.py

```

```
...\> runtests.py

```

## Writing Documentation[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#writing-documentation "Link to this heading")
This is a new feature, so it should be documented. Open the file `docs/topics/http/shortcuts.txt` and add the following at the end of the file:
```
``make_toast()``
================

.. function:: make_toast()

.. versionadded:: 2.2

Returns ``'toast'``.

```

Since this new feature will be in an upcoming release it is also added to the release notes for the next version of Django. Open the release notes for the latest version in `docs/releases/`, which at time of writing is `2.2.txt`. Add a note under the “Minor Features” header:
```
:mod:`django.shortcuts`
~~~~~~~~~~~~~~~~~~~~~~~

* The new :func:`django.shortcuts.make_toast` function returns ``'toast'``.

```

For more information on writing documentation, including an explanation of what the `versionadded` bit is all about, see [Writing documentation](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-documentation/). That page also includes an explanation of how to build a copy of the documentation locally, so you can preview the HTML that will be generated.
## Previewing your changes[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#previewing-your-changes "Link to this heading")
Now it’s time to review the changes made in the branch. To stage all the changes ready for commit, run:
/ 
```
$ git add --all

```

```
...\> git add --all

```

Then display the differences between your current copy of Django (with your changes) and the revision that you initially checked out earlier in the tutorial with:
/ 
```
$ git diff --cached

```

```
...\> git diff --cached

```

Use the arrow keys to move up and down.
```
diff --git a/django/shortcuts.py b/django/shortcuts.py
index 7ab1df0e9d..8dde9e28d9 100644
--- a/django/shortcuts.py
+++ b/django/shortcuts.py
@@ -156,3 +156,7 @@ def resolve_url(to, *args, **kwargs):

     # Finally, fall back and assume it's a URL
     return to
+
+
+def make_toast():
+    return 'toast'
diff --git a/docs/releases/2.2.txt b/docs/releases/2.2.txt
index 7d85d30c4a..81518187b3 100644
--- a/docs/releases/2.2.txt
+++ b/docs/releases/2.2.txt
@@ -40,6 +40,11 @@ database constraints. Constraints are added to models using the
 Minor features
 --------------

+:mod:`django.shortcuts`
+~~~~~~~~~~~~~~~~~~~~~~~
+
+* The new :func:`django.shortcuts.make_toast` function returns ``'toast'``.
+
 :mod:`django.contrib.admin`
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~

diff --git a/docs/topics/http/shortcuts.txt b/docs/topics/http/shortcuts.txt
index 7b3a3a2c00..711bf6bb6d 100644
--- a/docs/topics/http/shortcuts.txt
+++ b/docs/topics/http/shortcuts.txt
@@ -271,3 +271,12 @@ This example is equivalent to::
         my_objects = list(MyModel.objects.filter(published=True))
         if not my_objects:
             raise Http404("No MyModel matches the given query.")
+
+``make_toast()``
+================
+
+.. function:: make_toast()
+
+.. versionadded:: 2.2
+
+Returns ``'toast'``.
diff --git a/tests/shortcuts/test_make_toast.py b/tests/shortcuts/test_make_toast.py
new file mode 100644
index 0000000000..6f4c627b6e
--- /dev/null
+++ b/tests/shortcuts/test_make_toast.py
@@ -0,0 +1,7 @@
+from django.shortcuts import make_toast
+from django.test import SimpleTestCase
+
+
+class MakeToastTests(SimpleTestCase):
+    def test_make_toast(self):
+        self.assertEqual(make_toast(), 'toast')

```

When you’re done previewing the changes, hit the `q` key to return to the command line. If the diff looked okay, it’s time to commit the changes.
## Committing the changes[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#committing-the-changes "Link to this heading")
To commit the changes:
/ 
```
$ git commit

```

```
...\> git commit

```

This opens up a text editor to type the commit message. Follow the [commit message guidelines](https://docs.djangoproject.com/en/5.0/internals/contributing/committing-code/#committing-guidelines) and write a message like:
```
Fixed #99999 -- Added a shortcut function to make toast.

```

## Pushing the commit and making a pull request[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#pushing-the-commit-and-making-a-pull-request "Link to this heading")
After committing the changes, send it to your fork on GitHub (substitute “ticket_99999” with the name of your branch if it’s different):
/ 
```
$ git push origin ticket_99999

```

```
...\> git push origin ticket_99999

```

You can create a pull request by visiting the
Please don’t do it for this tutorial, but on the next page that displays a preview of the changes, you would click “Create pull request”.
## Next steps[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#next-steps "Link to this heading")
Congratulations, you’ve learned how to make a pull request to Django! Details of more advanced techniques you may need are in [Working with Git and GitHub](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/working-with-git/).
Now you can put those skills to good use by helping to improve Django’s codebase.
### More information for new contributors[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#more-information-for-new-contributors "Link to this heading")
Before you get too into contributing to Django, there’s a little more information on contributing that you should probably take a look at:
  * You should make sure to read Django’s documentation on [claiming tickets and submitting pull requests](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/submitting-patches/). It covers Trac etiquette, how to claim tickets for yourself, expected coding style (both for code and docs), and many other important details.
  * First time contributors should also read Django’s [documentation for first time contributors](https://docs.djangoproject.com/en/5.0/internals/contributing/new-contributors/). It has lots of good advice for those of us who are new to helping out with Django.
  * After those, if you’re still hungry for more information about contributing, you can always browse through the rest of [Django’s documentation on contributing](https://docs.djangoproject.com/en/5.0/internals/contributing/). It contains a ton of useful information and should be your first source for answering any questions you might have.


### Finding your first real ticket[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#finding-your-first-real-ticket "Link to this heading")
Once you’ve looked through some of that information, you’ll be ready to go out and find a ticket of your own to contribute to. Pay special attention to tickets with the “easy pickings” criterion. These tickets are often much simpler in nature and are great for first time contributors. Once you’re familiar with contributing to Django, you can start working on more difficult and complicated tickets.
If you just want to get started already (and nobody would blame you!), try taking a look at the list of [easy tickets without a branch](https://code.djangoproject.com/query?status=new&status=reopened&has_patch=0&easy=1&col=id&col=summary&col=status&col=owner&col=type&col=milestone&order=priority) and the [easy tickets that have branches which need improvement](https://code.djangoproject.com/query?status=new&status=reopened&needs_better_patch=1&easy=1&col=id&col=summary&col=status&col=owner&col=type&col=milestone&order=priority). If you’re familiar with writing tests, you can also look at the list of [easy tickets that need tests](https://code.djangoproject.com/query?status=new&status=reopened&needs_tests=1&easy=1&col=id&col=summary&col=status&col=owner&col=type&col=milestone&order=priority). Remember to follow the guidelines about claiming tickets that were mentioned in the link to Django’s documentation on [claiming tickets and submitting branches](https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/submitting-patches/).
### What’s next after creating a pull request?[¶](https://docs.djangoproject.com/en/5.0/intro/contributing/#what-s-next-after-creating-a-pull-request "Link to this heading")
After a ticket has a branch, it needs to be reviewed by a second set of eyes. After submitting a pull request, update the ticket metadata by setting the flags on the ticket to say “has patch”, “doesn’t need tests”, etc, so others can find it for review. Contributing doesn’t necessarily always mean writing code from scratch. Reviewing open pull requests is also a very helpful contribution. See [Triaging tickets](https://docs.djangoproject.com/en/5.0/internals/contributing/triaging-tickets/) for details.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/intro/whatsnext/)
[Using Django ](https://docs.djangoproject.com/en/5.0/topics/)
[](https://docs.djangoproject.com/en/5.0/intro/contributing/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Grand Comicbook Database donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Writing your first contribution for Django](https://docs.djangoproject.com/en/5.0/intro/contributing/)
    * [Introduction](https://docs.djangoproject.com/en/5.0/intro/contributing/#introduction)
      * [Who’s this tutorial for?](https://docs.djangoproject.com/en/5.0/intro/contributing/#who-s-this-tutorial-for)
      * [What does this tutorial cover?](https://docs.djangoproject.com/en/5.0/intro/contributing/#what-does-this-tutorial-cover)
    * [Code of Conduct](https://docs.djangoproject.com/en/5.0/intro/contributing/#code-of-conduct)
    * [Installing Git](https://docs.djangoproject.com/en/5.0/intro/contributing/#installing-git)
    * [Getting a copy of Django’s development version](https://docs.djangoproject.com/en/5.0/intro/contributing/#getting-a-copy-of-django-s-development-version)
      * [Creating projects with a local copy of Django](https://docs.djangoproject.com/en/5.0/intro/contributing/#creating-projects-with-a-local-copy-of-django)
    * [Running Django’s test suite for the first time](https://docs.djangoproject.com/en/5.0/intro/contributing/#running-django-s-test-suite-for-the-first-time)
    * [Working on a feature](https://docs.djangoproject.com/en/5.0/intro/contributing/#working-on-a-feature)
    * [Creating a branch](https://docs.djangoproject.com/en/5.0/intro/contributing/#creating-a-branch)
    * [Writing some tests for your ticket](https://docs.djangoproject.com/en/5.0/intro/contributing/#writing-some-tests-for-your-ticket)
      * [Writing a test for ticket #99999](https://docs.djangoproject.com/en/5.0/intro/contributing/#writing-a-test-for-ticket-99999)
      * [Running your new test](https://docs.djangoproject.com/en/5.0/intro/contributing/#running-your-new-test)
    * [Writing the code for your ticket](https://docs.djangoproject.com/en/5.0/intro/contributing/#writing-the-code-for-your-ticket)
    * [Running Django’s test suite for the second time](https://docs.djangoproject.com/en/5.0/intro/contributing/#running-django-s-test-suite-for-the-second-time)
    * [Writing Documentation](https://docs.djangoproject.com/en/5.0/intro/contributing/#writing-documentation)
    * [Previewing your changes](https://docs.djangoproject.com/en/5.0/intro/contributing/#previewing-your-changes)
    * [Committing the changes](https://docs.djangoproject.com/en/5.0/intro/contributing/#committing-the-changes)
    * [Pushing the commit and making a pull request](https://docs.djangoproject.com/en/5.0/intro/contributing/#pushing-the-commit-and-making-a-pull-request)
    * [Next steps](https://docs.djangoproject.com/en/5.0/intro/contributing/#next-steps)
      * [More information for new contributors](https://docs.djangoproject.com/en/5.0/intro/contributing/#more-information-for-new-contributors)
      * [Finding your first real ticket](https://docs.djangoproject.com/en/5.0/intro/contributing/#finding-your-first-real-ticket)
      * [What’s next after creating a pull request?](https://docs.djangoproject.com/en/5.0/intro/contributing/#what-s-next-after-creating-a-pull-request)


### Browse
  * Prev: [What to read next](https://docs.djangoproject.com/en/5.0/intro/whatsnext/)
  * Next: [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Getting started](https://docs.djangoproject.com/en/5.0/intro/)
      * Writing your first contribution for Django


### Getting help

[FAQ](https://docs.djangoproject.com/en/5.0/faq/)
    Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
    Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
    Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
    Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
    Report bugs with Django or Django documentation in our ticket tracker.
### Download:
Offline (Django 5.0): [HTML](https://media.djangoproject.com/docs/django-docs-5.0-en.zip) |
Provided by
### Diamond and Platinum Members
  * **JetBrains**


  * **Sentry**


  * **Kraken Tech**


## Django Links
### Learn More
  * [About Django](https://www.djangoproject.com/start/overview/)
  * [Getting Started with Django](https://www.djangoproject.com/start/)
  * [Team Organization](https://www.djangoproject.com/foundation/teams/)
  * [Django Software Foundation](https://www.djangoproject.com/foundation/)
  * [Code of Conduct](https://www.djangoproject.com/conduct/)
  * [Diversity Statement](https://www.djangoproject.com/diversity/)


### Get Involved
  * [Join a Group](https://www.djangoproject.com/community/)
  * [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
  * [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
  * [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
  * [Individual membership](https://www.djangoproject.com/foundation/individual-members/)


### Get Help
  * [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
  * [Django Discord](https://chat.djangoproject.com)
  * [Official Django Forum](https://forum.djangoproject.com/)


### Follow Us
  * [News RSS](https://www.djangoproject.com/rss/weblog/)


### Support Us
  * [Sponsor Django](https://www.djangoproject.com/fundraising/)
  * [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
  * [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)


[Django](https://www.djangoproject.com/)
  * Hosting by [In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
  * Design by &


© 2005-2026 [ Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.

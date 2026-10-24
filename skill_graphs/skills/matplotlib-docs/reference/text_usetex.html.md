[Skip to main content](https://matplotlib.org/stable/#main-content)
Back to top
`Ctrl`+`K`
[ ![Matplotlib 3.10.8 documentation - Home](https://matplotlib.org/stable/_static/logo_light.svg) ![Matplotlib 3.10.8 documentation - Home](https://matplotlib.org/stable/_static/logo_dark.svg) ](https://matplotlib.org/stable/)
  * [Plot types](https://matplotlib.org/stable/plot_types/index.html)
  * [User guide](https://matplotlib.org/stable/users/index.html)
  * [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
  * [Examples](https://matplotlib.org/stable/gallery/index.html)
  * [Reference](https://matplotlib.org/stable/api/index.html)
  * [Contribute](https://matplotlib.org/stable/devel/index.html)
  * [Releases](https://matplotlib.org/stable/users/release_notes.html)


3.10 (stable)
[3.10 (stable)](https://matplotlib.org/stable/index.html)[3.11 (dev)](https://matplotlib.org/devdocs/index.html)[3.9](https://matplotlib.org/3.9.3/index.html)[3.8](https://matplotlib.org/3.8.4/index.html)[3.7](https://matplotlib.org/3.7.5/index.html)[3.6](https://matplotlib.org/3.6.3/index.html)[3.5](https://matplotlib.org/3.5.3/index.html)[3.4](https://matplotlib.org/3.4.3/index.html)[3.3](https://matplotlib.org/3.3.4/index.html)[2.2](https://matplotlib.org/2.2.4/index.html)
  * [ Discourse](https://discourse.matplotlib.org)


  * [Plot types](https://matplotlib.org/stable/plot_types/index.html)
  * [User guide](https://matplotlib.org/stable/users/index.html)
  * [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
  * [Examples](https://matplotlib.org/stable/gallery/index.html)
  * [Reference](https://matplotlib.org/stable/api/index.html)
  * [Contribute](https://matplotlib.org/stable/devel/index.html)
  * [Releases](https://matplotlib.org/stable/users/release_notes.html)


3.10 (stable)
[3.10 (stable)](https://matplotlib.org/stable/index.html)[3.11 (dev)](https://matplotlib.org/devdocs/index.html)[3.9](https://matplotlib.org/3.9.3/index.html)[3.8](https://matplotlib.org/3.8.4/index.html)[3.7](https://matplotlib.org/3.7.5/index.html)[3.6](https://matplotlib.org/3.6.3/index.html)[3.5](https://matplotlib.org/3.5.3/index.html)[3.4](https://matplotlib.org/3.4.3/index.html)[3.3](https://matplotlib.org/3.3.4/index.html)[2.2](https://matplotlib.org/2.2.4/index.html)
  * [ Discourse](https://discourse.matplotlib.org)


### Cheatsheets
[ ![Matplotlib cheatsheets](https://matplotlib.org/stable/_static/mpl_cheatsheet1.png) ](https://matplotlib.org/cheatsheets/)
# Matplotlib 3.10.8 documentation[#](https://matplotlib.org/stable/#matplotlib-release-documentation "Link to this heading")
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations.
## Install[#](https://matplotlib.org/stable/#install "Link to this heading")
pip
```
pip install matplotlib

```
Copy to clipboard
conda
```
conda install -c conda-forge matplotlib

```
Copy to clipboard
pixi
```
pixi add matplotlib

```
Copy to clipboard
uv
```
uv add matplotlib

```
Copy to clipboard
Warning
uv usually installs its own versions of Python from the python-build-standalone project, and only recent versions of those Python builds (August 2025) work properly with the `tkagg` backend for displaying plots in a window. Please make sure you are using uv 0.8.7 or newer (update with e.g. `uv self update`) and that your bundled Python installs are up to date (with `uv python upgrade --reinstall`). Alternatively, you can use one of the other [supported GUI frameworks](https://matplotlib.org/stable/install/dependencies.html#optional-dependencies), e.g.
```
uv add matplotlib pyside6

```
Copy to clipboard
other
[Install an official release](https://matplotlib.org/stable/install/index.html#install-official)
[Third-party distributions](https://matplotlib.org/stable/install/index.html#install-third-party)
[Install a nightly build](https://matplotlib.org/stable/install/index.html#install-nightly-build)
[Install from source](https://matplotlib.org/stable/install/index.html#install-source)
## Learn[#](https://matplotlib.org/stable/#learn "Link to this heading")
**How to use Matplotlib?**
  * [Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)
  * [User guide](https://matplotlib.org/stable/users/index.html)
  * [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
  * [Frequently Asked Questions](https://matplotlib.org/stable/users/faq.html)


**What can Matplotlib do?**
  * [Plot types](https://matplotlib.org/stable/plot_types/index.html)
  * [Examples](https://matplotlib.org/stable/gallery/index.html)


**Reference**
  * [API reference](https://matplotlib.org/stable/api/index.html)
  * [Figure methods](https://matplotlib.org/stable/api/figure_api.html)
  * [Plotting methods](https://matplotlib.org/stable/api/axes_api.html)


Top-level interfaces to create:
  * figures: [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
  * subplots: [`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots"), [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")


## Community[#](https://matplotlib.org/stable/#community "Link to this heading")
  * [External resources](https://matplotlib.org/stable/users/resources/index.html)
    * [Books, chapters and articles](https://matplotlib.org/stable/users/resources/index.html#books-chapters-and-articles)
    * [Videos](https://matplotlib.org/stable/users/resources/index.html#videos)
    * [Tutorials](https://matplotlib.org/stable/users/resources/index.html#tutorials)
    * [Galleries](https://matplotlib.org/stable/users/resources/index.html#galleries)


[Third-party packages](https://matplotlib.org/mpl-third-party/),
provide custom, domain specific, and experimental features, including styles, colors, more plot types and backends, and alternative interfaces.
## What's new[#](https://matplotlib.org/stable/#what-s-new "Link to this heading")
Learn about new features and API changes.
  * [Release notes](https://matplotlib.org/stable/users/release_notes.html)


## Contribute[#](https://matplotlib.org/stable/#contribute "Link to this heading")
Matplotlib is a community project maintained for and by its users. See [Contribute](https://matplotlib.org/stable/devel/index.html#developers-guide-index) for the many ways you can help!
  * [Contribute](https://matplotlib.org/stable/devel/index.html)
    * [GitHub issue tracker](https://matplotlib.org/stable/devel/index.html#github-issue-tracker)
    * [Contributing guide](https://matplotlib.org/stable/devel/index.html#contributing-guide)
    * [Development workflow](https://matplotlib.org/stable/devel/index.html#development-workflow)
    * [Policies and guidelines](https://matplotlib.org/stable/devel/index.html#policies-and-guidelines)


## About us[#](https://matplotlib.org/stable/#about-us "Link to this heading")
Matplotlib was created by neurobiologist John Hunter to work with EEG data. It grew to be used and developed by many people in many different fields. John's goal was that Matplotlib make easy things easy and hard things possible.
  * [Project information](https://matplotlib.org/stable/project/index.html)
    * [Mission Statement](https://matplotlib.org/stable/project/mission.html)
    * [History](https://matplotlib.org/stable/project/history.html)
    * [Code of Conduct](https://matplotlib.org/stable/project/code_of_conduct.html)
    * [Citing Matplotlib](https://matplotlib.org/stable/project/citing.html)
    * [License](https://matplotlib.org/stable/project/license.html)
    * [Credits](https://matplotlib.org/stable/project/credits.html)


On this page
  * [Install](https://matplotlib.org/stable/#install)
  * [Learn](https://matplotlib.org/stable/#learn)
  * [Community](https://matplotlib.org/stable/#community)
  * [What's new](https://matplotlib.org/stable/#what-s-new)
  * [Contribute](https://matplotlib.org/stable/#contribute)
  * [About us](https://matplotlib.org/stable/#about-us)


© Copyright 2002–2012 John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team; 2012–2025 The Matplotlib development team.

Created using

Built from v3.10.8-7-g1957ba3918.

Built with the

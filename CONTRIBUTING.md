# Contributing to Coloi

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to Coloi and its packages. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[Contact us!](#solving-a-question)

[What should I know before I get started?](#what-should-i-know-before-i-get-started)
  * [Coloi and Packages](#atom-and-packages)
  * [Coloi Design Decisions](#design-decisions)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)

[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [Specs Styleguide](#specs-styleguide)
  * [Documentation Styleguide](#documentation-styleguide)

[Additional Notes](#additional-notes)
  * [Issue and Pull Request Labels](#issue-and-pull-request-labels)

## Solving a question!

> **Note:** Please don't file an issue to ask a question. You'll get faster results by using the resources below.

We have an official [Gitter Channel](https://goo.gl/4KVvfb) with a team to answer your doubts. And where the community chimes in with helpful advice if you have questions.

## What should I know before I get started?

### Coloi and it's Functions

Coloi is a small dorm-room open source project, eagerly accepting commits on better and bettter algorithms for Image Colorization. When you initially consider contributing to Coloi, you might be unsure about why are there codes written for face recognition and manipulation with webcam. This section should help you with that.

We want Coloi to Colorize || Decolorize Images and videos in every other way possible. 


![Colorize](https://goo.gl/iztnY2)

To get a sense for the functions that are bundled with Coloi, checkout the following list:

Here's a list of the big ones:

* [Colorize](#) - Can colorize black and white Images
* [Face-detection](#) - Can detect every niche of your face.

Also, because Atom is so extensible, it's possible that a feature you've become accustomed to in Atom or an issue you're encountering isn't coming from a bundled package at all, but rather a [community package](https://atom.io/packages) you've installed. Each community package has its own repository too, the [Atom FAQ](https://discuss.atom.io/c/faq) has instructions on how to [contact the maintainers of any Atom community package or theme.](https://discuss.atom.io/t/i-have-a-question-about-a-specific-atom-community-package-where-is-the-best-place-to-ask-it/25581)

#### Package Conventions

There are a few conventions that have developed over time around packages:

* Packages that add one or more syntax highlighting grammars are named `language-[language-name]`
    * Language packages can add other things besides just a grammar. Many offer commonly-used snippets. Try not to add too much though.
* Theme packages are split into two categories: UI and Syntax themes
    * UI themes are named `[theme-name]-ui`
    * Syntax themes are named `[theme-name]-syntax`
    * Often themes that are designed to work together are given the same root name, for example: `one-dark-ui` and `one-dark-syntax`
    * UI themes style everything outside of the editor pane &mdash; all of the green areas in the [packages image above](#atom-packages-image)
    * Syntax themes style just the items inside the editor pane, mostly syntax highlighting
* Packages that add [autocomplete providers](https://github.com/atom/autocomplete-plus/wiki/Autocomplete-Providers) are named `autocomplete-[what-they-autocomplete]` &mdash; ex: [autocomplete-css](https://github.com/atom/autocomplete-css)

### Design Decisions

When we make a significant decision in how we maintain the project and what we can or cannot support, we will document it in the [README.md](https://github.com/shravankumar9892/coloi/blob/master/README.md). If you have a question around how we do things, check [Gitter Channel](https://goo.gl/4KVvfb). 

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for Coloi. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check [this list](#before-submitting-a-bug-report) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-bug-report). Fill out [the required template](ISSUE_TEMPLATE.md), the information it asks for helps us resolve issues faster.

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### Before Submitting A Bug Report

* **Check the [Documentation](#).** You might be able to find the cause of the problem and fix things yourself. Most importantly, check if you can reproduce the problem [in the latest version of Coloi](#).
* **Check the [FAQs on the Gitter Channel](https://goo.gl/4KVvfb)** for a list of common questions and problems.
* **Perform a [cursory search](https://github.com/shravankumar9892/coloi/issues)** to see if the problem has already been reported. If it has **and the issue is still open**, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). After you've determined which function your bug is related to, create an issue on that function by mentioning it and provide the following information by filling in [the template](ISSUE_TEMPLATE.md).

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. aka. which command exactly you used in the terminal, or how you started Coloi otherwise. When listing steps, **don't just say what you did, but explain how you did it**.
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem. If you use the keyboard while following the steps, **record the GIF with the [Keybinding Resolver](https://github.com/atom/keybinding-resolver) shown**. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **If the problem is related to performance or memory**, include a [CPU profile capture](https://flight-manual.atom.io/hacking-atom/sections/debugging/#diagnose-runtime-performance) with your report.
* **If the problem wasn't triggered by a specific action**, describe what you were doing before the problem happened and share more information using the guidelines below.

Provide more context by answering these questions:

* **Did the problem start happening recently** (e.g. after updating to a new version of Coloi) or was this always a problem?
* If the problem started happening recently, **can you reproduce the problem in an older version of Coloi?** What's the most recent version in which the problem doesn't happen? You can download older versions of Coloi from [the releases page](#).
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.
* If the problem is related to working with files || webcam (e.g. opening and editing files), **does the problem happen for all files and projects or only some?** 

Include details about your configuration and environment:

* **Which version of Coloi are you using?** 
* **What's the name and version of the OS you're using**?
* **How many webcams do you open at a time? Does the problem occur at single webcam as well?**


### Suggesting Enhancements

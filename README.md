<p align="center">
    <a href="https://github.com/yisuschrist/iltransfer/issues">
        <img src="https://img.shields.io/github/issues/yisuschrist/iltransfer?color=171b20&label=Issues%20%20&logo=gnubash&labelColor=e05f65&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/iltransfer/forks">
        <img src="https://img.shields.io/github/forks/yisuschrist/iltransfer?color=171b20&label=Forks%20%20&logo=git&labelColor=f1cf8a&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/iltransfer/">
        <img src="https://img.shields.io/github/stars/yisuschrist/iltransfer?color=171b20&label=Stargazers&logo=octicon-star&labelColor=70a5eb">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/iltransfer/actions">
        <img alt="Tests Passing" src="https://github.com/yisuschrist/iltransfer/actions/workflows/github-code-scanning/codeql/badge.svg">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/iltransfer/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/yisuschrist/iltransfer?color=0088ff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://opensource.org/license/gpl-3-0/">
        <img alt="License" src="https://img.shields.io/github/license/yisuschrist/iltransfer?color=0088ff">
    </a>
</p>

<br>

<p align="center">
    <a href="https://github.com/yisuschrist/iltransfer/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/yisuschrist/iltransfer/issues/new/choose">Request Feature</a>
    ·
    <a href="https://github.com/yisuschrist/iltransfer/discussions">Ask Question</a>
    ·
    <a href="https://github.com/yisuschrist/iltransfer/security/policy#reporting-a-vulnerability">Report security bug</a>
</p>

<br>

![Alt](https://repobeats.axiom.co/api/embed/f6c38a416187bebbb4b7eb86c9a37fd23372f27b.svg "Repobeats analytics image")

<br>

Iltransfer (InstaLoader transfer) is a versatile Python application that streamlines the management of Instagram profile downloads using the [Instaloader](https://github.com/instaloader/instaloader) tool. With this program, you can effortlessly:

-   Transfer downloaded profiles to another destination when they are ready
-   Filter and move only the completed profiles, leaving incomplete downloads untouched.

Iltansfer is compatible with Windows, Linux and macOS, and it works seamlessly with Python 3.6 and above. Simplify your Instagram profile management with Iltransfer today!

<br>

<details>
<summary>Table of Contents</summary>

-   [Requirements](#requirements)
-   [Installation](#installation)
    -   [Manual installation](#manual-installation)
-   [Execution](#execution)
    -   [Example of execution](#example-of-execution)
-   [Contributors](#contributors)
    -   [How do I contribute to iltransfer?](#how-do-i-contribute-to-iltransfer)
-   [License](#license)
-   [TODO](#todo)

</details>

## Requirements

Here's a breakdown of the packages needed and their versions:

-   [platformdirs](https://pypi.org/project/platformdirs) - 3.10.0
-   [rich](https://pypi.org/project/rich) - 13.5.2
-   [rich-argparse-plus](https://pypi.org/project/rich-argparse-plus) - 0.3.1.4
-   [tqdm](https://pypi.org/project/tqdm) - 4.66.1

These packages can be installed using the following command:

This will install all the packages and their dependencies listed in the requirements.txt file. Make sure you have Python and pip installed on your system before running this command.

> [!NOTE]
> The software has been developed and tested using Python 3.11.4. The minimum required version to run the software is Python 3.6. Although the software may work with previous versions, it is not guaranteed.

## Installation

iltransfer can be installed easily as a Pypi package. Just run the following command:

```bash
pip3 install iltransfer
```

> [!IMPORTANT]
> For best practices and to avoid potential conflicts with your global Python environment, it is strongly recommended to install this program within a virtual environment. Avoid using the --user option for global installations. We highly recommend using [pipx](https://pypi.org/project/pipx) for a safe and isolated installation experience. Therefore, the appropriate command to install `iltransfer` would be:
>
> ```bash
> pipx install iltransfer
> ```

### Manual installation

If you prefer to install the program manually, follow these steps:

> [!WARNING]
> This will install the version from the latest commit, not the latest release.

1. Download the latest version of [iltransfer](https://github.com/yisuschrist/iltransfer) from this repository:

    ```bash
    git clone https://github.com/yisuschrist/iltransfer
    cd iltransfer
    ```

2. Install the dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

3. Run the following commands to install iltransfer in your `/usr/bin/` directory:

    ```bash
    sudo chmod +x iltransfer
    sudo cp iltransfer /usr/bin/
    ```

The program can now be ran from a terminal with the `iltransfer` command.

## Execution

To run the `iltransfer` script, you can use the following command:

```bash
iltransfer [OPTIONS]
```

where `[OPTIONS]` are the command line options described below:

```

```

#### Example of execution

## Contributors

<a href="https://github.com/yisuschrist/iltransfer/graphs/contributors"><img src="https://contrib.rocks/image?repo=yisuschrist/iltransfer" /></a>

### How do I contribute to iltransfer?

Before you participate in our delightful community, please read the [code of conduct](.github/CODE_OF_CONDUCT.md).

I'm far from being an expert and suspect there are many ways to improve – if you have ideas on how to make the configuration easier to maintain (and faster), don't hesitate to fork and send pull requests!

We also need people to test out pull requests. So take a look through [the open issues](https://github.com/yisuschrist/iltransfer/issues) and help where you can.

See [Contributing](.github/CONTRIBUTING.md) for more details.

## License

iltransfer is released under the [GPL-3.0 License](https://opensource.org/licenses/GPL-3.0).

## TODO

Planing to add the following features:

-   [x] Add a support to use config files (multi-platform) to store the options
-   [ ] Add a full documentation in Wiki section
-   [x] Add a Changelog / Release Notes

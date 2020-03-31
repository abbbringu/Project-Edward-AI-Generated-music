
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="img/music_notes_PNG64.png" alt="logo" width="100" height="200">
  </a>

  <h3 align="center">Project_Edward</h3>

  <p align="center">
    Ett program som genererar music!




<!-- TABLE OF CONTENTS -->
## Innehållsförteckning

* [Om Projektet](#om-projektet)
  * [Byggd Med](#byggd-med)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## Om Projektet

Projektet handlar om att skapa music utav ett dataset i form av midi. Filen ska helst vara ett instrument. Jag har gått igenom andra metoder som Lstm för att generera musik. Jag blev missnöjd med resultaten och bestämde att arbeta vidare. Lstm tog in massor med data och kan bestämma vilka noter som ska spelas efter på varandra. Konsekvensen blev att det inte gick att implemeterar durationer och pauser. 

För projektet har jag tänkt använda stylegan för att göra musik. Stylegan är teknisk sätt för bilder. Vilket vi kan använda. Därför använder vi midifiler. Man kan konvertera midifiler till ett kordinat system. X-axeln blir tid och Y axen blir noten. Vi kan spara koriatsystement som en png bild. Varje låt blir ungefär 5-50 bilder långa. Förhoppnings vis får vi ett bra resultat. En risk är att stylegan tar bilder oavsett vart i sången den är. Det vill säga att stylegan kommer inte uppfatta om en början och slut, allt är detsamma. 

<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="img/210appass_1_Piano_6.png" alt="logo" width="256" height="256">
</a>

Överblick av projektet:
* Samla in midi filer i formen (.mid) 
* Konverterar mid filerna till .png
* Gör om bilderna till ett data set (tfrecord) 
* Använd datasetet och börja träna
* Använd bilderna och minimera den till 100*106 res för att senare konvertera den till mid fil igen
Spela midifilerna

### Byggd Med
Här hittar du orginal koder som hjälpte med projektet.
* [Stylegan](https://github.com/t04glovern/stylegan-pokemon)
* [Midi2img and Img2midi](https://github.com/mathigatti/midi2img)
* [Resizing images](https://auth0.com/blog/image-processing-in-python-with-pillow/)



<!-- GETTING STARTED -->
## Getting Started

Det här projektet använder [datasetet](https://www.kaggle.com/soumikrakshit/classical-music-midi). Det här datasetet är klassisk musik som bara spelas av ett instrument. 

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
```sh
npm install npm@latest -g
```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
```sh
git clone https://github.com/your_username_/Project-Name.git
```
3. Install NPM packages
```sh
npm install
```
4. Enter your API in `config.js`
```JS
const API_KEY = 'ENTER YOUR API';
```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

const config = {
    // Enable this option will render markdown by pandoc instead of markdown-it.
    usePandocParser: false,

    // In Markdown, a single newline character doesn't cause a line break in the generated HTML. In GitHub Flavored Markdown, that is not true. Enable this config option to insert line breaks in rendered HTML for single newlines in Markdown source.
    breakOnSingleNewLine: true,

    // Enable smartypants and other sweet transforms.
    enableTypographer: false,

    // Enable conversion of URL-like text to links in the markdown preview.
    enableLinkify: true,

    // Math
    mathRenderingOption: "KaTeX", // "KaTeX" | "MathJax" | "None"
    mathInlineDelimiters: [
        ["$", "$"],
        ["\\(", "\\)"]
    ],
    mathBlockDelimiters: [
        ["$$", "$$"],
        ["\\[", "\\]"]
    ],
    mathRenderingOnLineService: "https://latex.codecogs.com/gif.latex", // "https://latex.codecogs.com/svg.latex", "https://latex.codecogs.com/png.latex"

    // Enable Wiki Link syntax support. More information can be found a  https://help.github.com/articles/adding-links-to-wikis/
    enableWikiLinkSyntax: true,
    // By default, the extension for wikilink is `.md`. For example: [[test]] will direct to file path `test.md`.
    wikiLinkFileExtension: '.md',


    // Enable extended table syntax to support merging table cells.
    enableExtendedTableSyntax: false,

    // Enable CriticMarkup syntax. Only works with markdown-it parser.
    // Please check http://criticmarkup.com/users-guide.php for more information.
    enableCriticMarkupSyntax: false,

    // Front matter rendering option
    frontMatterRenderingOption: 'none', // 'none' | 'table' | 'code block'

    // Mermaid theme
    mermaidTheme: 'mermaid.css', // 'mermaid.css' | 'mermaid.dark.css' | 'mermaid.forest.css'

    // Code Block theme
    // If `auto.css` is chosen, then the code block theme that best matches the current preview theme will be picked.
    codeBlockTheme: 'vs.css',
    //  "auto.css",
    //  "default.css",
    //  "atom-dark.css",
    //  "atom-light.css",
    //  "atom-material.css",
    //  "coy.css",
    //  "darcula.css",
    //  "dark.css",
    //  "funky.css",
    //  "github.css",
    //  "hopscotch.css",
    //  "monokai.css",
    //  "okaidia.css",
    //  "one-dark.css",
    //  "one-light.css",
    //  "pen-paper-coffee.css",
    //  "pojoaque.css",
    //  "solarized-dark.css",
    //  "solarized-light.css",
    //  "twilight.css",
    //  "vue.css",
    //  "vs.css",
    //  "xonokai.css"

    // Preview theme
    previewTheme: 'atom-light.css',
    // "atom-dark.css",
    // "atom-light.css",
    // "atom-material.css",
    // "github-dark.css",
    // "github-light.css",
    // "gothic.css",
    // "medium.css",
    // "monokai.css",
    // "newsprint.css",
    // "night.css",
    // "none.css",
    // "one-dark.css",
    // "one-light.css",
    // "solarized-dark.css",
    // "solarized-light.css",
    // "vue.css"

    // Revealjs presentation theme
    revealjsTheme: "white.css",
    // "beige.css",
    // "black.css",
    // "blood.css",
    // "league.css",
    // "moon.css",
    // "night.css",
    // "serif.css",
    // "simple.css",
    // "sky.css",
    // "solarized.css",
    // "white.css",
    // "none.css"

    // Accepted protocols for links.
    protocolsWhiteList: "http://, https://, atom://, file://, mailto:, tel:",

    // When using Image Helper to copy images, by default images will be copied to root image folder path '/assets'
    imageFolderPath: './_images',

    // Whether to print background for file export or not. If set to `false`, then `github-light` preview theme will b  used. You can also set `print_background` in front-matter for individual files.
    printBackground: true,

    // Chrome executable path, which is used for Puppeteer export. Leaving it empty means the path will be found automatically.
    chromePath: '',

    // ImageMagick command line path. Should be either `magick` or `convert`. Leaving it empty means the path will be found automatically.
    imageMagickPath: '',

    // Pandoc executable path
    pandocPath: 'pandoc',

    // Pandoc markdown flavor
    pandocMarkdownFlavor: "markdown-raw_tex+tex_math_single_backslash",

    // Pandoc arguments e.g. ['--smart', '--filter=/bin/exe']. Please use long argument names.
    pandocArguments: [],

    // Default latex engine for Pandoc export and latex code chunk.
    latexEngine: 'pdflatex',

    // Enables executing code chunks and importing javascript files.
    // ⚠ ️ Please use this feature with caution because it may put your security at risk!
    //    Your machine can get hacked if someone makes you open a markdown with malicious code while script execution is enabled.
    enableScriptExecution: false,

    // Enables transform audio video link to to html5 embed audio video tags.
    // Internally it enables markdown-it-html5-embed plugins.
    enableHTML5Embed: false,

    // Enables video/audio embed with ![]() syntax (default).
    HTML5EmbedUseImageSyntax: true,

    // Enables video/audio embed with []() syntax.
    HTML5EmbedUseLinkSyntax: false,

    // When true embed media with http:// schema in URLs. When false ignore and don't embed them.
    HTML5EmbedIsAllowedHttp: false,

    // HTML attributes to pass to audio tags.
    HTML5EmbedAudioAttributes: 'controls preload="metadata" width="320"',

    // HTML attributes to pass to video tags.
    HTML5EmbedVideoAttributes: 'controls preload="metadata" width="320" height="240"',

    // Puppeteer waits for a certain timeout in milliseconds before the document export.
    puppeteerWaitForTimeout: 0,

    // If set to true, then locally installed puppeteer-core will be required. Otherwise, the puppeteer globally installed by `npm install -g puppeteer` will be required.
    usePuppeteerCore: true
}

module.exports = {
    config
}

const mume = require("@shd101wyy/mume");
var config_file = require("./mume_config.js");

// es6
// import * as mume from "@shd101wyy/mume"

async function main(path) {
    await mume.init();

    const engine = new mume.MarkdownEngine({
        filePath: path,
        config: config_file.config
    });

    // html export
    await engine.htmlExport({
        offline: true,
        runAllCodeChunks: true
    });
    return process.exit();
}

// 获取命令以及当前文件名以外的参数list
var real_args = process.argv.splice(2)
path = real_args[0]
main(path);

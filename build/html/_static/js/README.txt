mermaid.min.mjs
==============

Mermaid 11.12.1，由 npm 包 mermaid@11.12.1 的 dist/mermaid.esm.mjs 用 esbuild 打包成单个 ESM 文件
（命令：esbuild node_modules/mermaid/dist/mermaid.esm.mjs --bundle --format=esm --minify --target=es2020）。

本地化目的：对外发布的文档站不依赖 CDN，内网/离线环境也能正常渲染时序图。
升级方式：替换 npm 包版本后重新执行上面的 esbuild 命令，并同步 source/conf.py 中的注释。

License: MIT，版权归 Mermaid 及其贡献者所有，见 https://github.com/mermaid-js/mermaid/blob/develop/LICENSE

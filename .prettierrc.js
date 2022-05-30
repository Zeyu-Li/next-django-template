module.exports = {
    printWidth: 100,
    tabWidth: 2,
    singleQuote: true,
    semi: false,
    trailingComma: 'es5',
    arrowParens: 'always',
    overrides: [
        {
            files: ['*.yml', '*.yaml'],
            options: {
                tabWidth: 4,
                bracketSpacing: false,
            },
        },
    ],
}

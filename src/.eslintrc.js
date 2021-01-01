module.exports = {
  env: {
    browser: true,
  },
  extends: [
    'plugin:vue/essential',
    'airbnb-base',
  ],
  parserOptions: {
    ecmaVersion: 11,
    sourceType: 'module',
  },
  plugins: [
    'vue',
  ],
  rules: {
    'linebreak-style': 'off',
  },
};

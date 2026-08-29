"use strict";

const assert = require("node:assert/strict");
const { status } = require("../src/index.js");

assert.equal(status(), "ok");
console.log("JavaScript smoke test: ok");

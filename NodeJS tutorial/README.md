# NodeJS tutorial


## 前言
Node.js 是 Ryan Dahl 基於 Google 的 V8 引擎於 2009 年釋出的一個 JavaScript 開發平台，主要聚焦於 Web 程式的開發，通常用被來寫網站。隨這近幾年發展迅速，也廣泛的在各領域上被使用，以Node的概念將自己視為應用上的一個點，點與點之間建構成強大的服務



## Features

* ### It is asynchronous and event Driven

  ```
  All APIs of Node.js library are asynchronous, that is, non-blocking. 
  It essentially means a Node.js based server never waits for an API to return data. 
  The server moves to the next API after calling it and a notificationmechanism of 
  Events of Node.js helps the server to get a response from the previous API call.
  ```

* ### Super Fast 

  ```
  Being built on Google Chrome’s V8 JavaScript Engine, Node.js is super efficient 
  and quick in code execution.
  ```

* ### Single Threaded but Highly Scalable

  ```
  Node.js uses a single threaded model with event looping. 
  Event mechanism helps the server to respond in a non-blocking way and makes the server highly scalable as opposed to traditional servers like Apache which create limited threads to handle requests.
  ```

* ### No Buffering

  ```
  Node.js applications never buffer any data. These applications simply output the 
  data in chunks.
  ```

  


## 事前準備
* [NPM](https://www.npmjs.com/)
    
    * Essential JavaScript development tools that help you go to market faster and build powerful applications using modern open source code.
    
* [NodeJS](https://nodejs.org/en/)

    * Make sure your nodeJS version is above 7.0 or download the recommended for most users version in the official website

* ES(ECMAScript) 6

    * [Class](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Classes)

    * Module (export, import)

      ```
      import "method_name" from "Module_name";
      ```

      ```
      export function func_name;
      export var name = "KE";
      ```

    * Arrow

      ```
      const setMyName = name => {
      	var myName = name
      	return myName
      }
      ```

    * Default values in function

      ```
      function setMyName(name="KE Jiang") {
      	...
      }
      
      And you can call this function by using
      
      setMyName() --> Will use the default name
      setMyName("Test Man") --> Will set the name parameter to "Test Man"
      ```

    * [Template literals](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Template_literals)

      ```
      var name = "my name is " + last_name + " " + first_name; 
      ```

    * [Destructuring assignment](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

    * [Spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

    * object shorthand (Make code more clear)

      * Not use ES6

      ```
      const name='KE',age='28',city='Tapei';
         
      const employee = {
          name: name,
          age: age,
          city: city
      };
      console.log(employee);//{name: "KE", age: "28", city: "Taipei"}
      ```

      * Use ES6

      ```
      const name='KE',age='28',city='Tapei';
         
      const employee = {
          name,
          age,
          city
      };
      console.log(employee);//{name: "KE", age: "28", city: "Taipei"}
      ```

    * [Promise](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Promise) ( Use to solve asynchronous events )
    * Support "const" and "let" syntax to define the local variable.

    

## Full-Stack Framework

* [Express](https://www.npmjs.com/package/express) 
  * Express is by far the most stable and widely used development framework, and is the only officially recommended web development framework for Node.js
* [Koa](https://www.npmjs.com/package/koa)
  * Expressive HTTP middleware framework for node.js to make web applications and APIs more enjoyable to write


## 任意門
| [回首頁](https://github.com/yuhioh217/Code-Tutorial) |  [下一頁]() | 



Authors
-
Copyright(c) 2017 KE Jiang<<yuihoh217@gmail.com>>
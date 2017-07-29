:Title: Behat, hoja trampa
:Slug: behat-hoja-trampa
:Date: 2017-07-29 00:03:22
:Category: cheatsheet 
:Tags: mink, behat, bdd

Command line (behat)
====================

.. code::

  --init                           Create the features directory
  --config=archivo.yml             Use config file
  --format=html -out=report.html   Html report
  --expand                         Display details
  --story-syntax --lang=es         Language
  --tags='@group1.@group2'         Return tests on groups

Feature
=======

.. code-block:: cucumber

    Feature: Descriptive text of what is desired
        In order to realize a named business value
        As an explicit system actor
        I want to ...

        Scenario: Some determinable business situation
            Given some precondition
            And some other precondition
            When some action by the actor
            And some other action
            And yet another action
            Then some testable outcome is achieved
            And something else we can check happens to

        Scenario: A diferent situation...

Behat in two words
==================

Behat automates the "acceptance testing" of the agile methodology "Scrum". Each
test is written in natural language with the gherkin syntax.

A feature is described by a <my-feature.feature> file. A feature is a set of
cases, called "scenarios".

Each scenario is defined by:

- Context (Given)
- Triggering events (When)
- An expected result (Then)

====== Use examples ======

.. code-block:: cucumber

    Scenario Outline: Some determinable bussiness situation
            Given I have <initialAmount> euros
            When I add <money> euros
            Then I should have now <finalAmount> euros

        Examples:
                | initialAmount | money     | finalAmount |
                | 15            | 5         | 20          |
                | 40            | 10        | 50          |
                | 20            | 5         | 25          |

Web apps (Mink)
===============

Surf

.. code-block:: cucumber

  I am on "url"
  I go to "url"
  I reload the page
  I move backward one page
  I move forward one page
  I press "button"
  I follow "link"

Forms

.. code-block:: cucumber

  I fill in "form_element" with "value"
  I fill in "value" for "form_element"
  I fill in the following
  I select "form_option" from "form_select"
  I additionally select "form_option" from "form_select"
  I check "form_checkbox"
  I uncheck "form_checkbox"
  I attach the file "/path/file.file" to "form_file"

Assertions

.. code-block:: cucumber

  I should see "content"
  the response should contain "content"
  I should not see "content"
  the response should not contain "content"
  the "form_element" field should contain "value"
  the "form_element" field should not contain "value"
  the "form_checkbox" checkbox should be checked
  the "form_checkbox" checkbox should not be checked
  I should be on "page"
  the url should match "url"
  the "num_position" element should contain "value"
  I should see "value" in the "element" element
  I should see an "element" element
  I should not see an "element" element
  I should see number "element" elements
  the response status code should be code

Mink Cheat Sheet
================

Session

.. code-block:: php

  $session = new \Behat\Mink\Session($driver);
  $session->start();   // start
  $session->reset();   // soft-reset:
  $session->restart(); // hard-reset:

  From the main context:
  $session = $this->getSession();

  From a sub-context
  $session = $this->getMainContext()->getSession();

  isStarted() Checks whether session was started
  start() Starts session
  stop() Stop session
  restart() Restart session
  reset() Reset session
  getPage() Returns page element
  getSelectorHandler() Returns Selector Handler
  visit($url) Visit specified URL
  setBasicAuth($u,$p) HTTP Basic authentification
  setRequestHeader($n,$v) Set request header
  getResponseHeaders() Get all response headers
  setCookie($n,$v) Sets cookie
  getCookie($n) Returns cookie
  getStatusCode() Returns response code
  getCurrentUrl() Returns current URL
  reload() Reload current page
  back() Moves backward
  forward() Move forward
  executeScript($script) Executes javascript
  evaluateScript($script) Returns javascript' response
  wait($time, $condition) Waits some time or until
  javascript condition is true

Available drivers

Goutte :
 https://github.com/fabpot/Goutte
Sahi :
 http://sourceforge.net/projects/sahi/
Zombie :
 http://zombie.labnotes.org/
Selenium (1 & 2 ) :
 http://seleniumhq.org/

Elements

.. code::

  $el->has($selector, $locator)
  $el->find($selector, $locator)
  $el->findAll($selector, $locator)
  $el->getText()
  $el->getHtml()

HTML nodes

.. code::

  $el->isVisible()
  $el->getValue()
  $el->getTagName()
  $el->getXpath()
  $el->hasAttribute($name)
  $el->getAttribute($name)

Forms

.. code::

  $el->press()
  $el->check()
  $el->uncheck()
  $el->isChecked()
  $el->selectOption($option, $multiple)
  $el->attachFile($path)
  $el->keypress()
  $el->keyDown()
  $el->keyUp()

Events

.. code::

  $el->click()
  $el->doubleClick()
  $el->rightClick()
  $el->mouseOver()
  $el->focus()
  $el->blur()
  $el->dragTo($element)


Default parameters <behat.yml>

.. code-block:: yml

  default:
   context:
   parameters:
   default_session: goutte
   javascript_session: sahi
   base_url: http://localhost
   browser: firefox
   goutte:
   zend_config:
   adapter:
  Zend\Http\Client\Adapter\Proxy
   proxy_host: host.com
   proxy_port: 8080
   sahi:
   host: localhost
   port: 9999
   zombie:
   host: 127.0.0.1
   port: 8124
   node_bin: node
   auto_server: true
   selenium:
   host: localhost
   port: 4444
   webdriver:
   host http://localhost:4444/wd/hub

from django.test import TestCase

# Create your tests here.
{% extends 'main/base.html' %}

{% block content %}

{% load static %}
<html lang="en">
  <head>
    <style>

      .card-full {
        max-width: 100% !important;
      }

      .img-responsive {
        max-width: 100% !important;
        height: auto !important;
        position: relative !important;
      }

      .form-check {
        align-items: end;
      }
      .pages {
        margin-left: 10px;
        margin-right: 10px;
        display: block;
      }

      .pagination {
        overflow: auto;
        display: flex;
        flex-wrap: wrap;
      }

      .top {
      position: sticky;
      bottom: 20px;
      place-self: end;
      text-decoration: none;
      padding: 10px;
      color: #FFFFFF;
      background: #000000;
      border-radius: 100px;

      --offset: 500px;
      margin-top: calc(100vh + var(--offset));
    }

      .top:hover {
        color: #E1DA22;
      }

      .container-top {
        text-align: end;

        --offset: 100px;
        --fade: 120px;

        mask: linear-gradient(#0000 calc(100vh + var(--offset)), #000 calc(100vh + var(--offset) + var(--fade)));
      }

      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      h1, h2{
        color: #618A5A;
      }

      p {
        margin-bottom: 0px;
      }

      .logocontainer img {
        text-align: center !important;
        width: 75vw;
      }

      .logocontainer {
        text-align: center;
        position: relative;
        width: 100% !important;
        max-width: 100% !important;
        margin: auto;
      }

      .cover-container .py-5 {
        padding-top: 0px !important;
      }

      .py-lg-5 {
        padding-top: 0px !important;
        padding-bottom: 0px !important;
      }

      .buffbutton {
        padding-bottom: 25px !important;
      }

      .btn {
        color: #FFFFFF;
        background-color: #E1DA22;
        font-size: 1rem !important;
        padding-left: 1em !important;
        padding-right: 1em !important;
      }

      .btn:hover {
        color: #E1DA22;
        background-color: #FFFFFF;
      }

      .py-5 {
        padding-bottom: 4rem !important;
      }

      .py-lg-5 a {
        display: inline-block;
        position: relative;
        z-index: 1;
        padding-left: 3em;
        padding-right: 3em;
        margin: -2em;
      }

      .navburg {
        position: absolute;
        background-color: #000000;
        z-index: 999;
      }

      .nav-item {
        background-color: #000000;
      }

      .logocontainer{
        padding-top: -10px;
      }

    .form-check {
      text-align: start !important;
      color: #FFFFFF;
    }

    .trade {
      margin: auto !important;
      white-space: nowrap !important;
      padding-left: 0px;
      padding-right: 0px;
    }

    .traderow {
      padding-left: 5px;
      padding-right: 5px;
      margin-left: 2.5px;
      margin-right: 2.5px;
    }

    .buy {
      background-color: #0000FF;
    }

    .sell {
      background-color: #EEDC5B;
    }

    .cancel {
      background-color: #FF0000;
    }

    p {
      color: #FFFFFF;
    }

    h5 {
      color: #E1DA22
    }

    p1 {
      font-size: 20px;
      color: #618A5A
    }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }

    blockquote {
      color: #888;
      margin: 20px 0 20px 20px;
    }

    blockquote:before,
    blockquote:after{
      content: '"';
    }

    @mixin uppercase {
      text-transform: uppercase;
    }

    @mixin center {
      margin: 0 auto;
    }

    /*.intro {
      position: relative;
      margin: 10px;
      width: 40%;
      height: auto;
      color: #444;
    }*/

    @mixin deck {
      position: relative;
      background: transparent;
      margin: 3em;
      width: 99%;
      height: auto;
    }

    @mixin card {
      position: relative;
      display: inline-block;
      background: transparent;
      background-color: #000;
      color: #000;
      width: 150px;
      height: 200px;
      margin-right: 20px;
      cursor: pointer;
    }


    .card {
      @include card;
    }

    .card .face {
      color: transparent;
      height: auto;

      text-align: center;
      text-transform: capitalize;
      box-shadow: 4px 4px 10px #555; /* Slim drop shadow so as not to bleed into the bounding box of the next card  */
    }

    .card .front {
      position: absolute;
      transform: rotateX(0deg) rotateY(0deg);
      transition: all .4s ease-in-out;
      backface-visibility: visible;
      z-index: 10;
    }

    .card {
      transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
      animation: drop3 .5s ease-in;
      background-color: transparent;
      color: transparent;
      height: auto;
    }

    .card-full {
      color: transparent;
    }

    .card .back {
      transform: rotateX(0deg) rotateY(180deg);
      transform-style: preserve-3d;
      transition: all .4s ease-in-out;
      backface-visibility: hidden;
      z-index: 5;
    }

    /* Flip the card and apply easing */
    .card.flip .front {
      transform: rotateY(180deg);
      transform-style: preserve-3d;
      transition: all .4s ease-in-out;
      backface-visibility: hidden;
      z-index: 900;
    }

    .card.flip .back {
      transform: rotateY(0deg);
      transform-style: preserve-3d;
      transition: all .4s ease-in-out;
      backface-visibility: visible;
      z-index: 1000;
    }

    .card-back {

      max-width: 100% !important;
      height: auto;
    }

  .buff-logo {
    height: 10vh;
  }

  .buff-num {
  background-color: #000000;
  margin-right: 5px;
  margin-left: 5px;
  font-size: 10px;
  width: 100% !important;
  height: 5vh;
}

.buff-num p {
  width: 100% !important;
  height: 3vh;
  line-height: 3vh;
}

.buff-score {
  background-color: #000000;
  margin-right: 5px;
  margin-left: 5px;
  font-size: 10px;
  width: 100% !important;
  height: 5vh;
}


 p-num {
   color: #C0A86D;
   position: absolute;
   top: 23%;
   left: 36%;
   font-size: 2rem
 }

 p-score {
   color: #C0A86D;
   position: absolute;
   top: 85%;
   left: 17.5%;
   font-size: 2rem
 }

.table>:not(caption)>*>* {
  padding-left: 0px !important;
  padding-right: 0px !important;
  padding-top: 0px !important;
  padding-bottom: 0px !important;
}

.table-responsive .container {
  padding-left: 1px !important;
  padding-right: 1px !important;
  margin-top: 10px !important;
}

.table {
  margin-top: 100px !important;
}

.thead-light {
  height: 4px !important;
}

.py-1 {
  padding-bottom: 0 !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
}

th {
  font-size: 8.5px;
}

tr {
  font-size: 8.5px;
  line-height: 12.5px;
}

td {
  line-height: 12.5px;
}




.buff-info {
  padding-top: 5px;
}

.form-check-label {
  color: #FFFFFF;
}

<style type="text/css">
.properties_table{
   min-height: 540px;
   font-size: 14px;
}


.big-box {
  margin-right: 0;
  margin-left: 0;
}

.buff-results {
  margin-right: 0;
  margin-left: 0;
}

.collapsible-link {
  width: 100%;
  position: relative;
  text-align: left;
  background-color: #000000;
  color: #FFFFFF;
  font-size: 36px;
}

.collapsible-link::before {
  content: "\f107";
  position: absolute;
  top: 50%;
  right: 0.8rem;
  transform: translateY(-50%);
  display: block;
  font-family: "FontAwesome";
  font-size: 1.1rem;
}

.collapsible-link[aria-expanded="true"]::before {
  content: "\f106";
}

.collapsed {
  border-bottom: 0.5px solid grey;
}

.form-check {
  color: #FFFFFF;
  font-size: 24px;
}

.trait-feature-row {
  border-bottom: 0.25px solid grey;
}

span > label {
  color: #000000 !important;
  font-size: 18px;
}

.btn-group {
  background-color: #000000;
  color: #FFFFFF;
}

.multiselect {
  background-color: #000000;
  color: #FFFFFF;
}

.multiselect-container {
  background-color: #000000;
  color: #FFFFFF;
}

.btn-group > .show {
  background-color: #FFFFFF;
  color: #000000;
}



/**
button[title="Graveyard"] {
  background: url('https://buffwild.b-cdn.net/Traits/Graveyard.png');
  background-repeat: no-repeat;
  background-position: 30px 0px;
  width: 32px;
  height: 32px;
}






 * Bootstrap Multiselect (http://davidstutz.de/bootstrap-multiselect/)
 *
 * Apache License, Version 2.0:
 * Copyright (c) 2012 - 2022 David Stutz
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a
 * copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 *
 * BSD 3-Clause License:
 * Copyright (c) 2012 - 2022 David Stutz
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *    - Redistributions of source code must retain the above copyright notice,
 *      this list of conditions and the following disclaimer.
 *    - Redistributions in binary form must reproduce the above copyright notice,
 *      this list of conditions and the following disclaimer in the documentation
 *      and/or other materials provided with the distribution.
 *    - Neither the name of David Stutz nor the names of its contributors may be
 *      used to endorse or promote products derived from this software without
 *      specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
 * OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 * ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
span.multiselect-native-select {
  position: relative;
}
span.multiselect-native-select select {
  border: 0 !important;
  clip: rect(0 0 0 0) !important;
  height: 1px !important;
  margin: -1px -1px -1px -3px !important;
  overflow: hidden !important;
  padding: 0 !important;
  position: absolute !important;
  width: 1px !important;
  left: 50%;
  top: 30px;
}
.multiselect.dropdown-toggle:after {
  display: none;
}
.multiselect {
  overflow: hidden;
  text-overflow: ellipsis;
}
.multiselect-container {
  position: absolute;
  list-style-type: none;
  margin: 0;
  padding: 0;
}
.multiselect-container .multiselect-reset .input-group {
  width: 93%;
}
.multiselect-container .multiselect-filter > .fa-search {
  z-index: 1;
  padding-left: 0.75rem;
}
.multiselect-container .multiselect-filter > input.multiselect-search {
  border: none;
  border-bottom: 1px solid lightgrey;
  padding-left: 2rem;
  margin-left: -1.625rem;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.multiselect-container .multiselect-filter > input.multiselect-search:focus {
  border-bottom-right-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem;
}
.multiselect-container .multiselect-filter > .multiselect-moz-clear-filter {
  margin-left: -1.5rem;
  display: none;
}
.multiselect-container .multiselect-option.multiselect-group-option-indented-full {
  padding-left: 2.6rem;
}
.multiselect-container .multiselect-option.multiselect-group-option-indented {
  padding-left: 1.8rem;
}
.multiselect-container .multiselect-group {
  cursor: pointer;
}
.multiselect-container .multiselect-group.closed .dropdown-toggle::after {
  transform: rotate(-90deg);
}
.multiselect-container .multiselect-group .caret-container ~ .form-check {
  margin-left: 0.5rem;
}
.multiselect-container .multiselect-option,
.multiselect-container .multiselect-group,
.multiselect-container .multiselect-all {
  padding: 0.25rem 0.25rem 0.25rem 0.75rem;
}
.multiselect-container .multiselect-option.dropdown-item,
.multiselect-container .multiselect-group.dropdown-item,
.multiselect-container .multiselect-all.dropdown-item,
.multiselect-container .multiselect-option.dropdown-toggle,
.multiselect-container .multiselect-group.dropdown-toggle,
.multiselect-container .multiselect-all.dropdown-toggle {
  cursor: pointer;
}
.multiselect-container .multiselect-option .form-check-label,
.multiselect-container .multiselect-group .form-check-label,
.multiselect-container .multiselect-all .form-check-label {
  cursor: pointer;
}
.multiselect-container .multiselect-option.active:not(.multiselect-active-item-fallback),
.multiselect-container .multiselect-group.active:not(.multiselect-active-item-fallback),
.multiselect-container .multiselect-all.active:not(.multiselect-active-item-fallback),
.multiselect-container .multiselect-option:not(.multiselect-active-item-fallback):active,
.multiselect-container .multiselect-group:not(.multiselect-active-item-fallback):active,
.multiselect-container .multiselect-all:not(.multiselect-active-item-fallback):active {
  background-color: lightgrey;
  color: black;
}
.multiselect-container .multiselect-option:hover,
.multiselect-container .multiselect-group:hover,
.multiselect-container .multiselect-all:hover,
.multiselect-container .multiselect-option:focus,
.multiselect-container .multiselect-group:focus,
.multiselect-container .multiselect-all:focus {
  background-color: darkgray !important;
}
.multiselect-container .multiselect-option .form-check,
.multiselect-container .multiselect-group .form-check,
.multiselect-container .multiselect-all .form-check {
  padding: 0 5px 0 20px;
}
.multiselect-container .multiselect-option:focus,
.multiselect-container .multiselect-group:focus,
.multiselect-container .multiselect-all:focus {
  outline: none;
}
.form-inline .multiselect-container span.form-check {
  padding: 3px 20px 3px 40px;
}
.input-group.input-group-sm > .multiselect-native-select .multiselect {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
  padding-right: 1.75rem;
  height: calc(1.5em + 0.5rem + 2px);
}
.input-group > .multiselect-native-select {
  flex: 1 1 auto;
  width: 1%;
}
.input-group > .multiselect-native-select > div.btn-group {
  width: 100%;
}
.input-group > .multiselect-native-select:not(:first-child) .multiselect {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}
.input-group > .multiselect-native-select:not(:last-child) .multiselect {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;



</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>

<script type="text/javascript" href="{% static 'main/js/bootstrap-multiselect.js' %}"></script>
<link rel="stylesheet" href="{% static 'main/css/bootstrap-multiselect.css' %}" type="text/css"/>

<link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/css/select2.min.css" rel="stylesheet" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/js/select2.min.js"></script>

<script>

  /**
   * Bootstrap Multiselect (http://davidstutz.de/bootstrap-multiselect/)
   *
   * Apache License, Version 2.0:
   * Copyright (c) 2012 - 2022 David Stutz
   *
   * Licensed under the Apache License, Version 2.0 (the "License"); you may not
   * use this file except in compliance with the License. You may obtain a
   * copy of the License at http://www.apache.org/licenses/LICENSE-2.0
   *
   * Unless required by applicable law or agreed to in writing, software
   * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
   * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
   * License for the specific language governing permissions and limitations
   * under the License.
   *
   * BSD 3-Clause License:
   * Copyright (c) 2012 - 2022 David Stutz
   * All rights reserved.
   *
   * Redistribution and use in source and binary forms, with or without
   * modification, are permitted provided that the following conditions are met:
   *    - Redistributions of source code must retain the above copyright notice,
   *      this list of conditions and the following disclaimer.
   *    - Redistributions in binary form must reproduce the above copyright notice,
   *      this list of conditions and the following disclaimer in the documentation
   *      and/or other materials provided with the distribution.
   *    - Neither the name of David Stutz nor the names of its contributors may be
   *      used to endorse or promote products derived from this software without
   *      specific prior written permission.
   *
   * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
   * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
   * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
   * PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
   * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
   * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
   * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
   * OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
   * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
   * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
   * ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
   */
  (function (root, factory) {
      // check to see if 'knockout' AMD module is specified if using requirejs
      if (typeof define === 'function' && define.amd &&
          typeof require === 'function' && typeof require.specified === 'function' && require.specified('knockout')) {

          // AMD. Register as an anonymous module.
          define(['jquery', 'knockout'], factory);
      } else {
          // Browser globals
          factory(root.jQuery, root.ko);
      }
  })(this, function ($, ko) {
      "use strict";// jshint ;_;

      if (typeof ko !== 'undefined' && ko.bindingHandlers && !ko.bindingHandlers.multiselect) {
          ko.bindingHandlers.multiselect = {
              after: ['options', 'value', 'selectedOptions', 'enable', 'disable'],

              init: function (element, valueAccessor, allBindings, viewModel, bindingContext) {
                  var $element = $(element);
                  var config = ko.toJS(valueAccessor());

                  $element.multiselect(config);

                  if (allBindings.has('options')) {
                      var options = allBindings.get('options');
                      if (ko.isObservable(options)) {
                          ko.computed({
                              read: function () {
                                  options();
                                  setTimeout(function () {
                                      var ms = $element.data('multiselect');
                                      if (ms)
                                          ms.updateOriginalOptions();//Not sure how beneficial this is.
                                      $element.multiselect('rebuild');
                                  }, 1);
                              },
                              disposeWhenNodeIsRemoved: element
                          });
                      }
                  }

                  //value and selectedOptions are two-way, so these will be triggered even by our own actions.
                  //It needs some way to tell if they are triggered because of us or because of outside change.
                  //It doesn't loop but it's a waste of processing.
                  if (allBindings.has('value')) {
                      var value = allBindings.get('value');
                      if (ko.isObservable(value)) {
                          ko.computed({
                              read: function () {
                                  value();
                                  setTimeout(function () {
                                      $element.multiselect('refresh');
                                  }, 1);
                              },
                              disposeWhenNodeIsRemoved: element
                          }).extend({ rateLimit: 100, notifyWhenChangesStop: true });
                      }
                  }

                  //Switched from arrayChange subscription to general subscription using 'refresh'.
                  //Not sure performance is any better using 'select' and 'deselect'.
                  if (allBindings.has('selectedOptions')) {
                      var selectedOptions = allBindings.get('selectedOptions');
                      if (ko.isObservable(selectedOptions)) {
                          ko.computed({
                              read: function () {
                                  selectedOptions();
                                  setTimeout(function () {
                                      $element.multiselect('refresh');
                                  }, 1);
                              },
                              disposeWhenNodeIsRemoved: element
                          }).extend({ rateLimit: 100, notifyWhenChangesStop: true });
                      }
                  }

                  var setEnabled = function (enable) {
                      setTimeout(function () {
                          if (enable)
                              $element.multiselect('enable');
                          else
                              $element.multiselect('disable');
                      });
                  };

                  if (allBindings.has('enable')) {
                      var enable = allBindings.get('enable');
                      if (ko.isObservable(enable)) {
                          ko.computed({
                              read: function () {
                                  setEnabled(enable());
                              },
                              disposeWhenNodeIsRemoved: element
                          }).extend({ rateLimit: 100, notifyWhenChangesStop: true });
                      } else {
                          setEnabled(enable);
                      }
                  }

                  if (allBindings.has('disable')) {
                      var disable = allBindings.get('disable');
                      if (ko.isObservable(disable)) {
                          ko.computed({
                              read: function () {
                                  setEnabled(!disable());
                              },
                              disposeWhenNodeIsRemoved: element
                          }).extend({ rateLimit: 100, notifyWhenChangesStop: true });
                      } else {
                          setEnabled(!disable);
                      }
                  }

                  ko.utils.domNodeDisposal.addDisposeCallback(element, function () {
                      $element.multiselect('destroy');
                  });
              },

              update: function (element, valueAccessor, allBindings, viewModel, bindingContext) {
                  var $element = $(element);
                  var config = ko.toJS(valueAccessor());

                  $element.multiselect('setOptions', config);
                  $element.multiselect('rebuild');
              }
          };
      }

      function forEach(array, callback) {
          for (var index = 0; index < array.length; ++index) {
              callback(array[index], index);
          }
      }

      var multiselectCount = 0;

      /**
       * Constructor to create a new multiselect using the given select.
       *
       * @param {jQuery} select
       * @param {Object} options
       * @returns {Multiselect}
       */
      function Multiselect(select, options) {

          this.$select = $(select);
          this.options = this.mergeOptions($.extend({}, options, this.$select.data()));

          // Placeholder via data attributes
          if (this.$select.attr("data-placeholder")) {
              this.options.nonSelectedText = this.$select.data("placeholder");
          }

          // Initialization.
          // We have to clone to create a new reference.
          this.originalOptions = this.$select.clone()[0].options;
          this.query = '';
          this.searchTimeout = null;
          this.lastToggledInput = null;
          this.multiselectId = this.generateUniqueId() + '_' + multiselectCount;
          this.internalIdCount = 0;

          this.options.multiple = this.$select.attr('multiple') === "multiple";
          this.options.onChange = $.proxy(this.options.onChange, this);
          this.options.onSelectAll = $.proxy(this.options.onSelectAll, this);
          this.options.onDeselectAll = $.proxy(this.options.onDeselectAll, this);
          this.options.onDropdownShow = $.proxy(this.options.onDropdownShow, this);
          this.options.onDropdownHide = $.proxy(this.options.onDropdownHide, this);
          this.options.onDropdownShown = $.proxy(this.options.onDropdownShown, this);
          this.options.onDropdownHidden = $.proxy(this.options.onDropdownHidden, this);
          this.options.onInitialized = $.proxy(this.options.onInitialized, this);
          this.options.onFiltering = $.proxy(this.options.onFiltering, this);

          // Build select all if enabled.
          this.buildContainer();
          this.buildButton();
          this.buildDropdown();
          this.buildReset();
          this.buildSelectAll();
          this.buildDropdownOptions();
          this.buildFilter();
          this.buildButtons();

          this.updateButtonText();
          this.updateSelectAll(true);

          if (this.options.enableClickableOptGroups && this.options.multiple) {
              this.updateOptGroups();
          }

          this.options.wasDisabled = this.$select.prop('disabled');
          if (this.options.disableIfEmpty && $('option', this.$select).length <= 0 && !this.options.wasDisabled) {
              this.disable(true);
          }

          this.$select.wrap('<span class="multiselect-native-select" />').after(this.$container);
          this.$select.prop('tabindex', '-1');

          if (this.options.widthSynchronizationMode !== 'never') {
              this.synchronizeButtonAndPopupWidth();
          }

          this.$select.data('multiselect', this);
          this.options.onInitialized(this.$select, this.$container);
      }

      Multiselect.prototype = {

          defaults: {
              /**
               * Default text function will either print 'None selected' in case no
               * option is selected or a list of the selected options up to a length
               * of 3 selected options.
               *
               * @param {jQuery} options
               * @param {jQuery} select
               * @returns {String}
               */
              buttonText: function (selectedOptions, select) {
                var text_i_want = 'Specific ⌄';
                return text_i_want;
              },
              /**
               * Updates the title of the button similar to the buttonText function.
               *
               * @param {jQuery} options
               * @param {jQuery} select
               * @returns {@exp;selected@call;substr}
               */
              buttonTitle: function (options, select) {
                  return 'Specific';
                },
              checkboxName: function (option) {
                  return false; // no checkbox name
              },
              /**
               * Create a label.
               *
               * @param {jQuery} element
               * @returns {String}
               */
              optionLabel: function (element) {
                  return $(element).attr('label') || $(element).text();
              },
              /**
               * Create a class.
               *
               * @param {jQuery} element
               * @returns {String}
               */
              optionClass: function (element) {
                  return $(element).attr('class') || '';
              },
              /**
               * Triggered on change of the multiselect.
               *
               * Not triggered when selecting/deselecting options manually.
               *
               * @param {jQuery} option
               * @param {Boolean} checked
               */
              onChange: function (option, checked) {

              },
              /**
               * Triggered when the dropdown is shown.
               *
               * @param {jQuery} event
               */
              onDropdownShow: function (event) {

              },
              /**
               * Triggered when the dropdown is hidden.
               *
               * @param {jQuery} event
               */
              onDropdownHide: function (event) {

              },
              /**
               * Triggered after the dropdown is shown.
               *
               * @param {jQuery} event
               */
              onDropdownShown: function (event) {

              },
              /**
               * Triggered after the dropdown is hidden.
               *
               * @param {jQuery} event
               */
              onDropdownHidden: function (event) {

              },
              /**
               * Triggered on select all.
               */
              onSelectAll: function (selectedOptions) {

              },
              /**
               * Triggered on deselect all.
               */
              onDeselectAll: function (deselectedOptions) {

              },
              /**
               * Triggered after initializing.
               *
               * @param {jQuery} $select
               * @param {jQuery} $container
               */
              onInitialized: function ($select, $container) {

              },
              /**
               * Triggered on filtering.
               *
               * @param {jQuery} $filter
               */
              onFiltering: function ($filter) {

              },
              enableHTML: false,
              buttonClass: 'custom-select',
              inheritClass: false,
              buttonWidth: 'auto',
              buttonContainer: '<div class="btn-group" />',
              dropRight: false,
              dropUp: false,
              selectedClass: 'active',
              // Maximum height of the dropdown menu.
              // If maximum height is exceeded a scrollbar will be displayed.
              maxHeight: null,
              includeSelectAllOption: false,
              includeSelectAllIfMoreThan: 0,
              selectAllText: ' Select all',
              selectAllValue: 'multiselect-all',
              selectAllName: false,
              selectAllNumber: true,
              selectAllJustVisible: true,
              enableFiltering: false,
              enableCaseInsensitiveFiltering: false,
              enableFullValueFiltering: false,
              enableClickableOptGroups: false,
              enableCollapsibleOptGroups: false,
              collapseOptGroupsByDefault: false,
              filterPlaceholder: 'Search',
              // possible options: 'text', 'value', 'both'
              filterBehavior: 'text',
              includeFilterClearBtn: true,
              preventInputChangeEvent: false,
              nonSelectedText: 'None Selected',
              nSelectedText: 'selected',
              allSelectedText: 'All selected',
              resetButtonText: 'Reset',
              numberDisplayed: 3,
              disableIfEmpty: false,
              disabledText: '',
              delimiterText: ', ',
              includeResetOption: false,
              includeResetDivider: false,
              resetText: 'Reset',
              indentGroupOptions: true,
              // possible options: 'never', 'always', 'ifPopupIsSmaller', 'ifPopupIsWider'
              widthSynchronizationMode: 'never',
              // possible options: 'left', 'center', 'right'
              buttonTextAlignment: 'center',
              enableResetButton: false,
              templates: {
                  button: '<button type="button" class="multiselect dropdown-toggle" data-toggle="dropdown"><span class="multiselect-selected-text"></span></button>',
                  popupContainer: '<div class="multiselect-container dropdown-menu"></div>',
                  filter: '<div class="multiselect-filter d-flex align-items-center"><i class="fas fa-sm fa-search text-muted"></i><input type="search" class="multiselect-search form-control" /></div>',
                  buttonGroup: '<div class="multiselect-buttons btn-group" style="display:flex;"></div>',
                  buttonGroupReset: '<button type="button" class="multiselect-reset btn btn-secondary btn-block"></button>',
                  option: '<button type="button" class="multiselect-option dropdown-item"></button>',
                  divider: '<div class="dropdown-divider"></div>',
                  optionGroup: '<button type="button" class="multiselect-group dropdown-item"></button>',
                  resetButton: '<div class="multiselect-reset text-center p-2"><button type="button" class="btn btn-sm btn-block btn-outline-secondary"></button></div>'
              }
          },

          constructor: Multiselect,

          /**
           * Builds the container of the multiselect.
           */
          buildContainer: function () {
              this.$container = $(this.options.buttonContainer);
              if (this.options.widthSynchronizationMode !== 'never') {
                  this.$container.on('show.bs.dropdown', $.proxy(function () {
                      // the width needs to be synchronized again in case the width of the button changed in between
                      this.synchronizeButtonAndPopupWidth();
                      this.options.onDropdownShow();
                  }, this));
              }
              else {
                  this.$container.on('show.bs.dropdown', this.options.onDropdownShow);
              }
              this.$container.on('hide.bs.dropdown', this.options.onDropdownHide);
              this.$container.on('shown.bs.dropdown', this.options.onDropdownShown);
              this.$container.on('hidden.bs.dropdown', this.options.onDropdownHidden);
          },

          /**
           * Builds the button of the multiselect.
           */
          buildButton: function () {
              this.$button = $(this.options.templates.button).addClass(this.options.buttonClass);
              if (this.$select.attr('class') && this.options.inheritClass) {
                  this.$button.addClass(this.$select.attr('class'));
              }
              // Adopt active state.
              if (this.$select.prop('disabled')) {
                  this.disable();
              }
              else {
                  this.enable();
              }

              // Manually add button width if set.
              if (this.options.buttonWidth && this.options.buttonWidth !== 'auto') {
                  this.$button.css({
                      'width': '100%' //this.options.buttonWidth,
                  });
                  this.$container.css({
                      'width': this.options.buttonWidth
                  });
              }

              if (this.options.buttonTextAlignment) {
                  switch (this.options.buttonTextAlignment) {
                      case 'left':
                          this.$button.addClass('text-left');
                          break;
                      case 'center':
                          this.$button.addClass('text-center');
                          break;
                      case 'right':
                          this.$button.addClass('text-right');
                          break;
                  }
              }

              // Keep the tab index from the select.
              var tabindex = this.$select.attr('tabindex');
              if (tabindex) {
                  this.$button.attr('tabindex', tabindex);
              }

              this.$container.prepend(this.$button);
          },

          /**
           * Builds the popup container representing the dropdown menu.
           */
          buildDropdown: function () {

              // Build popup container.
              this.$popupContainer = $(this.options.templates.popupContainer);

              if (this.options.dropRight) {
                  this.$container.addClass('dropright');
              }
              else if (this.options.dropUp) {
                  this.$container.addClass("dropup");
              }

              // Set max height of dropdown menu to activate auto scrollbar.
              if (this.options.maxHeight) {
                  // TODO: Add a class for this option to move the css declarations.
                  this.$popupContainer.css({
                      'max-height': this.options.maxHeight + 'px',
                      'overflow-y': 'auto',
                      'overflow-x': 'hidden'
                  });
              }

              if (this.options.widthSynchronizationMode !== 'never') {
                  this.$popupContainer.css('overflow-x', 'hidden');
              }

              this.$popupContainer.on("touchstart click", function (e) {
                  e.stopPropagation();
              });

              this.$container.append(this.$popupContainer);
          },

          synchronizeButtonAndPopupWidth: function () {
              if (!this.$popupContainer || this.options.widthSynchronizationMode === 'never') {
                  return;
              }

              var buttonWidth = this.$button.outerWidth();
              switch (this.options.widthSynchronizationMode) {
                  case 'always':
                      this.$popupContainer.css('min-width', buttonWidth);
                      this.$popupContainer.css('max-width', buttonWidth);
                      break;
                  case 'ifPopupIsSmaller':
                      this.$popupContainer.css('min-width', buttonWidth);
                      break;
                  case 'ifPopupIsWider':
                      this.$popupContainer.css('max-width', buttonWidth);
                      break;
              }
          },

          /**
           * Build the dropdown options and binds all necessary events.
           *
           * Uses createDivider and createOptionValue to create the necessary options.
           */
          buildDropdownOptions: function () {

              this.$select.children().each($.proxy(function (index, element) {

                  var $element = $(element);
                  // Support optgroups and options without a group simultaneously.
                  var tag = $element.prop('tagName')
                      .toLowerCase();

                  if ($element.prop('value') === this.options.selectAllValue) {
                      return;
                  }

                  if (tag === 'optgroup') {
                      this.createOptgroup(element);
                  }
                  else if (tag === 'option') {

                      if ($element.data('role') === 'divider') {
                          this.createDivider();
                      }
                      else {
                          this.createOptionValue(element, false);
                      }

                  }

                  // Other illegal tags will be ignored.
              }, this));

              // Bind the change event on the dropdown elements.
              $(this.$popupContainer).off('change', '> *:not(.multiselect-group) input[type="checkbox"], > *:not(.multiselect-group) input[type="radio"]');
              $(this.$popupContainer).on('change', '> *:not(.multiselect-group) input[type="checkbox"], > *:not(.multiselect-group) input[type="radio"]', $.proxy(function (event) {
                  var $target = $(event.target);

                  var checked = $target.prop('checked') || false;
                  var isSelectAllOption = $target.val() === this.options.selectAllValue;

                  // Apply or unapply the configured selected class.
                  if (this.options.selectedClass) {
                      if (checked) {
                          $target.closest('.multiselect-option')
                              .addClass(this.options.selectedClass);
                      }
                      else {
                          $target.closest('.multiselect-option')
                              .removeClass(this.options.selectedClass);
                      }
                  }

                  // Get the corresponding option.
                  var id = $target.attr('id');
                  var $option = this.getOptionById(id);

                  var $optionsNotThis = $('option', this.$select).not($option);
                  var $checkboxesNotThis = $('input', this.$container).not($target);

                  if (isSelectAllOption) {

                      if (checked) {
                          this.selectAll(this.options.selectAllJustVisible, true);
                      }
                      else {
                          this.deselectAll(this.options.selectAllJustVisible, true);
                      }
                  }
                  else {
                      if (checked) {
                          $option.prop('selected', true);

                          if (this.options.multiple) {
                              // Simply select additional option.
                              $option.prop('selected', true);
                          }
                          else {
                              // Unselect all other options and corresponding checkboxes.
                              if (this.options.selectedClass) {
                                  $($checkboxesNotThis).closest('.dropdown-item').removeClass(this.options.selectedClass);
                              }

                              $($checkboxesNotThis).prop('checked', false);
                              $optionsNotThis.prop('selected', false);

                              // It's a single selection, so close.
                              this.$button.click();
                          }

                          if (this.options.selectedClass === "active") {
                              $optionsNotThis.closest(".dropdown-item").css("outline", "");
                          }
                      }
                      else {
                          // Unselect option.
                          $option.prop('selected', false);
                      }

                      // To prevent select all from firing onChange: #575
                      this.options.onChange($option, checked);

                      // Do not update select all or optgroups on select all change!
                      this.updateSelectAll();

                      if (this.options.enableClickableOptGroups && this.options.multiple) {
                          this.updateOptGroups();
                      }
                  }

                  this.$select.change();
                  this.updateButtonText();

                  if (this.options.preventInputChangeEvent) {
                      return false;
                  }
              }, this));

              $('.multiselect-option', this.$popupContainer).off('mousedown');
              $('.multiselect-option', this.$popupContainer).on('mousedown', function (e) {
                  if (e.shiftKey) {
                      // Prevent selecting text by Shift+click
                      return false;
                  }
              });

              $(this.$popupContainer).off('touchstart click', '.multiselect-option, .multiselect-all, .multiselect-group');
              $(this.$popupContainer).on('touchstart click', '.multiselect-option, .multiselect-all, .multiselect-group', $.proxy(function (event) {
                  event.stopPropagation();

                  var $target = $(event.target);

                  if (event.shiftKey && this.options.multiple) {
                      if (!$target.is("input")) { // Handles checkbox selection manually (see https://github.com/davidstutz/bootstrap-multiselect/issues/431)
                          event.preventDefault();
                          $target = $target.closest(".multiselect-option").find("input");
                          $target.prop("checked", !$target.prop("checked"));
                      }
                      var checked = $target.prop('checked') || false;

                      if (this.lastToggledInput !== null && this.lastToggledInput !== $target) { // Make sure we actually have a range
                          var from = this.$popupContainer.find(".multiselect-option:visible").index($target.closest(".multiselect-option"));
                          var to = this.$popupContainer.find(".multiselect-option:visible").index(this.lastToggledInput.closest(".multiselect-option"));

                          if (from > to) { // Swap the indices
                              var tmp = to;
                              to = from;
                              from = tmp;
                          }

                          // Make sure we grab all elements since slice excludes the last index
                          ++to;

                          // Change the checkboxes and underlying options
                          var range = this.$popupContainer.find(".multiselect-option:not(.multiselect-filter-hidden)").slice(from, to).find("input");

                          range.prop('checked', checked);

                          if (this.options.selectedClass) {
                              range.closest('.multiselect-option')
                                  .toggleClass(this.options.selectedClass, checked);
                          }

                          for (var i = 0, j = range.length; i < j; i++) {
                              var $checkbox = $(range[i]);

                              var $option = this.getOptionById($checkbox.attr('id'));

                              $option.prop('selected', checked);
                          }
                      }

                      // Trigger the select "change" event
                      $target.trigger("change");
                  }
                  else if (!$target.is('input')) {
                      var $checkbox = $target.closest('.multiselect-option, .multiselect-all').find('.form-check-input');
                      if ($checkbox.length > 0) {
                          if (this.options.multiple || !$checkbox.prop('checked')) {
                              $checkbox.prop('checked', !$checkbox.prop('checked'));
                              $checkbox.change();
                          }
                      }
                      else if (this.options.enableClickableOptGroups && this.options.multiple && !$target.hasClass("caret-container")) {
                          var groupItem = $target;
                          if (!groupItem.hasClass("multiselect-group")) {
                              groupItem = $target.closest('.multiselect-group');
                          }
                          $checkbox = groupItem.find(".form-check-input");
                          if ($checkbox.length > 0) {
                              $checkbox.prop('checked', !$checkbox.prop('checked'));
                              $checkbox.change();
                          }
                      }

                      event.preventDefault();
                  }

                  // Remembers last clicked option
                  var $input = $target.closest(".multiselect-option").find("input[type='checkbox'], input[type='radio']");
                  if ($input.length > 0) {
                      this.lastToggledInput = $target;
                  }
                  else {
                      this.lastToggledInput = null;
                  }

                  $target.blur();
              }, this));

              //Keyboard support.
              this.$container.off('keydown.multiselect').on('keydown.multiselect', $.proxy(function (event) {
                  var $items = $(this.$container).find(".multiselect-option:not(.disabled), .multiselect-group:not(.disabled), .multiselect-all").filter(":visible");
                  var index = $items.index($items.filter(':focus'));
                  var $search = $('.multiselect-search', this.$container);

                  // keyCode 9 == Tab
                  if (event.keyCode === 9 && this.$container.hasClass('show')) {
                      this.$button.click();
                  }
                  // keyCode 13 = Enter
                  else if (event.keyCode == 13) {
                      var $current = $items.eq(index);
                      setTimeout(function () {
                          $current.focus();
                      }, 1);
                  }
                  // keyCode 38 = Arrow Up
                  else if (event.keyCode == 38) {
                      if (index == 0 && !$search.is(':focus')) {
                          setTimeout(function () {
                              $search.focus();
                          }, 1);
                      }
                  }
                  // keyCode 40 = Arrow Down
                  else if (event.keyCode == 40) {
                      if ($search.is(':focus')) {
                          var $first = $items.eq(0);
                          setTimeout(function () {
                              $search.blur();
                              $first.focus();
                          }, 1);
                      }
                      else if (index == -1) {
                          setTimeout(function () {
                              $search.focus();
                          }, 1);
                      }
                  }
              }, this));

              if (this.options.enableClickableOptGroups && this.options.multiple) {
                  $(".multiselect-group input", this.$popupContainer).off("change");
                  $(".multiselect-group input", this.$popupContainer).on("change", $.proxy(function (event) {
                      event.stopPropagation();

                      var $target = $(event.target);
                      var checked = $target.prop('checked') || false;

                      var $item = $(event.target).closest('.dropdown-item');
                      var $group = $item.nextUntil(".multiselect-group")
                          .not('.multiselect-filter-hidden')
                          .not('.disabled');

                      var $inputs = $group.find("input");

                      var $options = [];

                      if (this.options.selectedClass) {
                          if (checked) {
                              $item.addClass(this.options.selectedClass);
                          }
                          else {
                              $item.removeClass(this.options.selectedClass);
                          }
                      }

                      $.each($inputs, $.proxy(function (index, input) {
                          var $input = $(input);
                          var id = $input.attr('id');
                          var $option = this.getOptionById(id);

                          if (checked) {
                              $input.prop('checked', true);
                              $input.closest('.dropdown-item')
                                  .addClass(this.options.selectedClass);

                              $option.prop('selected', true);
                          }
                          else {
                              $input.prop('checked', false);
                              $input.closest('.dropdown-item')
                                  .removeClass(this.options.selectedClass);

                              $option.prop('selected', false);
                          }

                          $options.push($option);
                      }, this))

                      // Cannot use select or deselect here because it would call updateOptGroups again.

                      this.options.onChange($options, checked);

                      this.$select.change();
                      this.updateButtonText();
                      this.updateSelectAll();
                  }, this));
              }

              if (this.options.enableCollapsibleOptGroups) {
                  let clickableSelector = this.options.enableClickableOptGroups
                      ? ".multiselect-group .caret-container"
                      : ".multiselect-group";

                  $(clickableSelector, this.$popupContainer).off("click");
                  $(clickableSelector, this.$popupContainer).on("click", $.proxy(function (event) {
                      var $group = $(event.target).closest('.multiselect-group');
                      var $inputs = $group.nextUntil(".multiselect-group").not('.multiselect-filter-hidden');

                      var visible = true;
                      $inputs.each(function () {
                          visible = visible && !$(this).hasClass('multiselect-collapsible-hidden');
                      });

                      if (visible) {
                          $inputs.hide().addClass('multiselect-collapsible-hidden');
                          $group.get(0).classList.add("closed");
                      } else {
                          $inputs.show().removeClass('multiselect-collapsible-hidden');
                          $group.get(0).classList.remove("closed");
                      }
                  }, this));
              }
          },

          /**
           * Create a checkbox container with input and label based on given values
           * @param {JQuery} $item
           * @param {String} label
           * @param {String} name
           * @param {String} value
           * @param {String} inputType
           * @returns {JQuery}
           */
          createCheckbox: function ($item, labelContent, name, value, title, inputType, internalId) {
              var $wrapper = $('<span />');
              $wrapper.addClass("form-check");

              var $checkboxLabel = $('<label class="form-check-label" />');
              if (this.options.enableHTML && $(labelContent).length > 0) {
                  $checkboxLabel.html(labelContent);
              }
              else {
                  $checkboxLabel.text(labelContent);
              }
              $wrapper.append($checkboxLabel);

              var $checkbox = $('<input class="form-check-input"/>').attr('type', inputType);
              $checkbox.val(value);
              $wrapper.prepend($checkbox);

              if (internalId) {
                  $checkbox.attr('id', internalId);
                  $checkboxLabel.attr('for', internalId);
              }

              if (name) {
                  $checkbox.attr('name', name);
              }

              $item.prepend($wrapper);
              $item.attr("title", title || labelContent);

              return $checkbox;
          },

          /**
           * Create an option using the given select option.
           *
           * @param {jQuery} element
           */
          createOptionValue: function (element, isGroupOption) {
              var $element = $(element);
              if ($element.is(':selected')) {
                  $element.prop('selected', true);
              }

              // Support the label attribute on options.
              var label = this.options.optionLabel(element);
              var classes = this.options.optionClass(element);
              var value = $element.val();
              var inputType = this.options.multiple ? "checkbox" : "radio";
              var title = $element.attr('title');

              var $option = $(this.options.templates.option);
              $option.addClass(classes);

              if (isGroupOption && this.options.indentGroupOptions) {
                  if (this.options.enableCollapsibleOptGroups) {
                      $option.addClass("multiselect-group-option-indented-full")
                  }
                  else {
                      $option.addClass("multiselect-group-option-indented");
                  }
              }

              // Hide all children items when collapseOptGroupsByDefault is true
              if (this.options.collapseOptGroupsByDefault && $(element).parent().prop("tagName").toLowerCase() === "optgroup") {
                  $option.addClass("multiselect-collapsible-hidden");
                  $option.hide();
              }

              var name = this.options.checkboxName($element);

              var checkboxId = this.createAndApplyUniqueId($element);
              var $checkbox = this.createCheckbox($option, label, name, value, title, inputType, checkboxId);

              var selected = $element.prop('selected') || false;

              if (value === this.options.selectAllValue) {
                  $option.addClass("multiselect-all");
                  $option.removeClass("multiselect-option");
                  $checkbox.parent().parent()
                      .addClass('multiselect-all');
              }

              this.$popupContainer.append($option);

              if ($element.is(':disabled')) {
                  $checkbox.attr('disabled', 'disabled')
                      .prop('disabled', true)
                      .closest('.dropdown-item')
                      .addClass('disabled');
              }

              $checkbox.prop('checked', selected);

              if (selected && this.options.selectedClass) {
                  $checkbox.closest('.dropdown-item')
                      .addClass(this.options.selectedClass);
              }
          },

          /**
           * Creates a divider using the given select option.
           *
           * @param {jQuery} element
           */
          createDivider: function (element) {
              var $divider = $(this.options.templates.divider);
              this.$popupContainer.append($divider);
          },

          /**
           * Creates an optgroup.
           *
           * @param {jQuery} group
           */
          createOptgroup: function (group) {
              var $group = $(group);
              var label = $group.attr("label");
              var value = $group.attr("value");
              var title = $group.attr('title');

              var $groupOption = $("<span class='multiselect-group dropdown-item-text'></span>");

              if (this.options.enableClickableOptGroups && this.options.multiple) {
                  $groupOption = $(this.options.templates.optionGroup);
                  var checkboxId = this.createAndApplyUniqueId($group);
                  var $checkbox = this.createCheckbox($groupOption, label, null, value, title, "checkbox", checkboxId);
              }
              else {
                  if (this.options.enableHTML) {
                      $groupOption.html(" " + label);
                  }
                  else {
                      $groupOption.text(" " + label);
                  }
              }

              var classes = this.options.optionClass(group);
              $groupOption.addClass(classes);

              if (this.options.enableCollapsibleOptGroups) {
                  $groupOption.find('.form-check').addClass('d-inline-block');
                  $groupOption.get(0).insertAdjacentHTML("afterbegin", '<span class="caret-container dropdown-toggle"></span>');
              }

              if ($group.is(':disabled')) {
                  $groupOption.addClass('disabled');
              }

              this.$popupContainer.append($groupOption);

              $("option", group).each($.proxy(function ($, group) {
                  this.createOptionValue(group, true);
              }, this));
          },

          /**
           * Build the reset.
           *
           */
          buildReset: function () {
              if (this.options.includeResetOption) {

                  // Check whether to add a divider after the reset.
                  if (this.options.includeResetDivider) {
                      var divider = $(this.options.templates.divider);
                      divider.addClass("mt-0");
                      this.$popupContainer.prepend(divider);
                  }

                  var $resetButton = $(this.options.templates.resetButton);

                  if (this.options.enableHTML) {
                      $('button', $resetButton).html(this.options.resetText);
                  }
                  else {
                      $('button', $resetButton).text(this.options.resetText);
                  }

                  $('button', $resetButton).click($.proxy(function () {
                      this.clearSelection();
                  }, this));

                  this.$popupContainer.prepend($resetButton);
              }
          },

          /**
           * Build the select all.
           *
           * Checks if a select all has already been created.
           */
          buildSelectAll: function () {
              if (typeof this.options.selectAllValue === 'number') {
                  this.options.selectAllValue = this.options.selectAllValue.toString();
              }

              var alreadyHasSelectAll = this.hasSelectAll();

              if (!alreadyHasSelectAll && this.options.includeSelectAllOption && this.options.multiple
                  && $('option', this.$select).length > this.options.includeSelectAllIfMoreThan) {

                  // Check whether to add a divider after the select all.
                  if (this.options.includeSelectAllDivider) {
                      this.$popupContainer.prepend($(this.options.templates.divider));
                  }

                  var $option = $(this.options.templates.li || this.options.templates.option);
                  var $checkbox = this.createCheckbox($option, this.options.selectAllText, this.options.selectAllName,
                      this.options.selectAllValue, this.options.selectAllText, "checkbox", this.createAndApplyUniqueId(null));

                  $option.addClass("multiselect-all");
                  $option.removeClass("multiselect-option");
                  $option.find(".form-check-label").addClass("font-weight-bold");

                  this.$popupContainer.prepend($option);

                  $checkbox.prop('checked', false);
              }
          },

          /**
           * Builds the filter.
           */
          buildFilter: function () {

              // Build filter if filtering OR case insensitive filtering is enabled and the number of options exceeds (or equals) enableFilterLength.
              if (this.options.enableFiltering || this.options.enableCaseInsensitiveFiltering) {
                  var enableFilterLength = Math.max(this.options.enableFiltering, this.options.enableCaseInsensitiveFiltering);

                  if (this.$select.find('option').length >= enableFilterLength) {

                      this.$filter = $(this.options.templates.filter);
                      $('input', this.$filter).attr('placeholder', this.options.filterPlaceholder);

                      // Handles optional filter clear button
                      if (!this.options.includeFilterClearBtn) {
                          this.$filter.find(".multiselect-search").attr("type", "text");

                          // Remove clear button if the old design of the filter with input groups and separated clear button is used
                          this.$filter.find(".multiselect-clear-filter").remove();
                      }
                      else {
                          // Firefox does not support a clear button in search inputs right now therefore it must be added manually
                          if (this.isFirefox() && this.$filter.find(".multiselect-clear-filter").length === 0) {
                              this.$filter.append("<i class='fas fa-times text-muted multiselect-clear-filter multiselect-moz-clear-filter'></i>");
                          }

                          this.$filter.find(".multiselect-clear-filter").on('click', $.proxy(function (event) {
                              clearTimeout(this.searchTimeout);

                              this.query = '';
                              this.$filter.find('.multiselect-search').val('');
                              $('.dropdown-item', this.$popupContainer).show().removeClass('multiselect-filter-hidden');

                              this.updateSelectAll();

                              if (this.options.enableClickableOptGroups && this.options.multiple) {
                                  this.updateOptGroups();
                              }

                          }, this));
                      }

                      this.$popupContainer.prepend(this.$filter);

                      this.$filter.val(this.query).on('click', function (event) {
                          event.stopPropagation();
                      }).on('input keydown', $.proxy(function (event) {
                          // Cancel enter key default behaviour
                          if (event.which === 13) {
                              event.preventDefault();
                          }

                          if (this.isFirefox() && this.options.includeFilterClearBtn) {
                              if (event.target.value) {
                                  this.$filter.find(".multiselect-moz-clear-filter").show();
                              }
                              else {
                                  this.$filter.find(".multiselect-moz-clear-filter").hide();
                              }
                          }

                          // This is useful to catch "keydown" events after the browser has updated the control.
                          clearTimeout(this.searchTimeout);

                          this.searchTimeout = this.asyncFunction($.proxy(function () {

                              if (this.query !== event.target.value) {
                                  this.query = event.target.value;

                                  var currentGroup, currentGroupVisible;
                                  $.each($('.multiselect-option, .multiselect-group', this.$popupContainer), $.proxy(function (index, element) {
                                      var value = $('input', element).length > 0 ? $('input', element).val() : "";
                                      var text = $('.form-check-label', element).text();

                                      var filterCandidate = '';
                                      if ((this.options.filterBehavior === 'text')) {
                                          filterCandidate = text;
                                      }
                                      else if ((this.options.filterBehavior === 'value')) {
                                          filterCandidate = value;
                                      }
                                      else if (this.options.filterBehavior === 'both') {
                                          filterCandidate = text + '\n' + value;
                                      }

                                      if (value !== this.options.selectAllValue && text) {

                                          // By default lets assume that element is not
                                          // interesting for this search.
                                          var showElement = false;

                                          if (this.options.enableCaseInsensitiveFiltering) {
                                              filterCandidate = filterCandidate.toLowerCase();
                                              this.query = this.query.toLowerCase();
                                          }

                                          if (this.options.enableFullValueFiltering && this.options.filterBehavior !== 'both') {
                                              var valueToMatch = filterCandidate.trim().substring(0, this.query.length);
                                              if (this.query.indexOf(valueToMatch) > -1) {
                                                  showElement = true;
                                              }
                                          }
                                          else if (filterCandidate.indexOf(this.query) > -1) {
                                              showElement = true;
                                          }

                                          // Toggle current element (group or group item) according to showElement boolean.
                                          if (!showElement) {
                                              $(element).css('display', 'none');
                                              $(element).addClass('multiselect-filter-hidden');
                                          }
                                          if (showElement) {
                                              $(element).css('display', 'block');
                                              $(element).removeClass('multiselect-filter-hidden');
                                          }

                                          // Differentiate groups and group items.
                                          if ($(element).hasClass('multiselect-group')) {
                                              // Remember group status.
                                              currentGroup = element;
                                              currentGroupVisible = showElement;
                                          }
                                          else {
                                              // Show group name when at least one of its items is visible.
                                              if (showElement) {
                                                  $(currentGroup).show()
                                                      .removeClass('multiselect-filter-hidden');
                                              }

                                              // Show all group items when group name satisfies filter.
                                              if (!showElement && currentGroupVisible) {
                                                  $(element).show()
                                                      .removeClass('multiselect-filter-hidden');
                                              }
                                          }
                                      }
                                  }, this));
                              }

                              this.updateSelectAll();

                              if (this.options.enableClickableOptGroups && this.options.multiple) {
                                  this.updateOptGroups();
                              }

                              this.updatePopupPosition();

                              this.options.onFiltering(event.target);

                          }, this), 300, this);
                      }, this));
                  }
              }
          },

          /**
           * Builds the filter.
           */
          buildButtons: function () {
              if (this.options.enableResetButton) {
                  var $buttonGroup = $(this.options.templates.buttonGroup);
                  this.$buttonGroupReset = $(this.options.templates.buttonGroupReset).text(this.options.resetButtonText);
                  $buttonGroup.append(this.$buttonGroupReset);
                  this.$popupContainer.prepend($buttonGroup);

                  // We save all options that were previously selected.
                  this.defaultSelection = {};
                  $('option', this.$select).each($.proxy(function (index, element) {
                      var $option = $(element);
                      this.defaultSelection[$option.val()] = $option.prop('selected');
                  }, this));

                  this.$buttonGroupReset.on('click', $.proxy(function (event) {
                      $('option', this.$select).each($.proxy(function (index, element) {
                          var $option = $(element);
                          $option.prop('selected', this.defaultSelection[$option.val()]);
                      }, this));
                      this.refresh();

                      if (this.options.enableFiltering) {
                          this.$filter.trigger('keydown');
                          $('input', this.$filter).val('');
                      }
                  }, this));
              }
          },

          updatePopupPosition: function () {
              // prevent gaps between popup and select when filter is used (#1199)
              var transformMatrix = this.$popupContainer.css("transform");
              var matrixType = transformMatrix.substring(0, transformMatrix.indexOf('('));
              var values = transformMatrix.substring(transformMatrix.indexOf('(') + 1, transformMatrix.length - 1);
              var valuesArray = values.split(',');

              var valueIndex = 5;
              if (matrixType === "matrix3d") {
                  valueIndex = 13;
              }

              if (valuesArray.length < valueIndex) {
                  return;
              }

              var yTransformation = valuesArray[valueIndex];
              // Need to check to avoid errors when testing and in some other situations.
              yTransformation = typeof yTransformation === 'undefined' ? 0 : yTransformation.trim();
              if (yTransformation < 0) {
                  yTransformation = this.$popupContainer.css("height").replace('px', '') * -1;
                  valuesArray[valueIndex] = yTransformation;
                  transformMatrix = matrixType + '(' + valuesArray.join(',') + ')';
                  this.$popupContainer.css("transform", transformMatrix);
              }
          },

          /**
           * Unbinds the whole plugin.
           */
          destroy: function () {
              this.$container.remove();
              this.$select.unwrap();
              this.$select.show();

              // reset original state
              this.$select.prop('disabled', this.options.wasDisabled);
              this.$select.find('option, optgroup').removeAttr('data-multiselectid');
              this.$select.data('multiselect', null);
          },

          /**
           * Refreshs the multiselect based on the selected options of the select.
           */
          refresh: function () {
              var inputs = {};
              $('.multiselect-option input', this.$popupContainer).each(function () {
                  inputs[$(this).val()] = $(this);
              });

              $('option', this.$select).each($.proxy(function (index, element) {
                  var $elem = $(element);
                  var $input = inputs[$(element).val()];

                  if ($elem.is(':selected')) {
                      $input.prop('checked', true);

                      if (this.options.selectedClass) {
                          $input.closest('.multiselect-option')
                              .addClass(this.options.selectedClass);
                      }
                  }
                  else {
                      $input.prop('checked', false);

                      if (this.options.selectedClass) {
                          $input.closest('.multiselect-option')
                              .removeClass(this.options.selectedClass);
                      }
                  }

                  if ($elem.is(":disabled")) {
                      $input.attr('disabled', 'disabled')
                          .prop('disabled', true)
                          .closest('.multiselect-option')
                          .addClass('disabled');
                  }
                  else {
                      $input.prop('disabled', false)
                          .closest('.multiselect-option')
                          .removeClass('disabled');
                  }
              }, this));

              this.updateButtonText();
              this.updateSelectAll();

              if (this.options.enableClickableOptGroups && this.options.multiple) {
                  this.updateOptGroups();
              }
          },

          /**
           * Select all options of the given values.
           *
           * If triggerOnChange is set to true, the on change event is triggered if
           * and only if one value is passed.
           *
           * @param {Array} selectValues
           * @param {Boolean} triggerOnChange
           */
          select: function (selectValues, triggerOnChange) {
              if (!$.isArray(selectValues)) {
                  selectValues = [selectValues];
              }

              for (var i = 0; i < selectValues.length; i++) {
                  var value = selectValues[i];

                  if (value === null || value === undefined) {
                      continue;
                  }

                  var $checkboxes = this.getInputsByValue(value);
                  if (!$checkboxes || $checkboxes.length === 0) {
                      continue;
                  }

                  for (var checkboxIndex = 0; checkboxIndex < $checkboxes.length; ++checkboxIndex) {
                      var $checkbox = $checkboxes[checkboxIndex];

                      var $option = this.getOptionById($checkbox.attr('id'));
                      if ($option === undefined) {
                          continue;
                      }

                      if (this.options.selectedClass) {
                          $checkbox.closest('.dropdown-item')
                              .addClass(this.options.selectedClass);
                      }

                      $checkbox.prop('checked', true);
                      $option.prop('selected', true);

                      if (!this.options.multiple) {
                          var $checkboxesNotThis = $('input', this.$container).not($checkbox);
                          $($checkboxesNotThis).prop('checked', false);
                          $($checkboxesNotThis).closest('.multiselect-option').removeClass("active")

                          var $optionsNotThis = $('option', this.$select).not($option);
                          $optionsNotThis.prop('selected', false);
                      }

                      if (triggerOnChange) {
                          this.options.onChange($option, true);
                      }
                  }
              }

              this.updateButtonText();
              this.updateSelectAll();

              if (this.options.enableClickableOptGroups && this.options.multiple) {
                  this.updateOptGroups();
              }
          },

          /**
           * Clears all selected items.
           */
          clearSelection: function () {
              this.deselectAll(false);
              this.updateButtonText();
              this.updateSelectAll();

              if (this.options.enableClickableOptGroups && this.options.multiple) {
                  this.updateOptGroups();
              }
          },

          /**
           * Deselects all options of the given values.
           *
           * If triggerOnChange is set to true, the on change event is triggered, if
           * and only if one value is passed.
           *
           * @param {Array} deselectValues
           * @param {Boolean} triggerOnChange
           */
          deselect: function (deselectValues, triggerOnChange) {
              if (!this.options.multiple) {
                  // In single selection mode at least on option needs to be selected
                  return;
              }

              if (!$.isArray(deselectValues)) {
                  deselectValues = [deselectValues];
              }

              for (var i = 0; i < deselectValues.length; i++) {
                  var value = deselectValues[i];

                  if (value === null || value === undefined) {
                      continue;
                  }

                  var $checkboxes = this.getInputsByValue(value);
                  if (!$checkboxes || $checkboxes.length === 0) {
                      continue;
                  }

                  for (var checkboxIndex = 0; checkboxIndex < $checkboxes.length; ++checkboxIndex) {
                      var $checkbox = $checkboxes[checkboxIndex];

                      var $option = this.getOptionById($checkbox.attr('id'));
                      if (!$option) {
                          continue;
                      }

                      if (this.options.selectedClass) {
                          $checkbox.closest('.dropdown-item')
                              .removeClass(this.options.selectedClass);
                      }

                      $checkbox.prop('checked', false);
                      $option.prop('selected', false);

                      if (triggerOnChange) {
                          this.options.onChange($option, false);
                      }
                  }
              }

              this.updateButtonText();
              this.updateSelectAll();

              if (this.options.enableClickableOptGroups && this.options.multiple) {
                  this.updateOptGroups();
              }
          },

          /**
           * Selects all enabled & visible options.
           *
           * If justVisible is true or not specified, only visible options are selected.
           *
           * @param {Boolean} justVisible
           * @param {Boolean} triggerOnSelectAll
           */
          selectAll: function (justVisible, triggerOnSelectAll) {
              if (!this.options.multiple) {
                  // In single selection mode only one option can be selected at a time
                  return;
              }

              // Record all changes, i.e., options selected that were not selected before.
              var selected = [];
              var justVisible = typeof justVisible === 'undefined' ? true : justVisible;

              if (justVisible) {
                  var visibleOptions = $(".multiselect-option:not(.disabled):not(.multiselect-filter-hidden)", this.$popupContainer);
                  $('input:enabled', visibleOptions).prop('checked', true);
                  visibleOptions.addClass(this.options.selectedClass);

                  $('input:enabled', visibleOptions).each($.proxy(function (index, element) {
                      var id = $(element).attr('id');
                      var option = this.getOptionById(id);
                      if (!$(option).prop('selected')) {
                          selected.push(option);
                      }
                      $(option).prop('selected', true);
                  }, this));
              }
              else {
                  var allOptions = $(".multiselect-option:not(.disabled)", this.$popupContainer);
                  $('input:enabled', allOptions).prop('checked', true);
                  allOptions.addClass(this.options.selectedClass);

                  $('input:enabled', allOptions).each($.proxy(function (index, element) {
                      var id = $(element).attr('id');
                      var option = this.getOptionById(id);
                      if (!$(option).prop('selected')) {
                          selected.push(option);
                      }
                      $(option).prop('selected', true);
                  }, this));
              }

              $('.multiselect-option input[value="' + this.options.selectAllValue + '"]', this.$popupContainer).prop('checked', true);

              if (this.options.enableClickableOptGroups && this.options.multiple) {
                  this.updateOptGroups();
              }

              this.updateButtonText();
              this.updateSelectAll();

              if (triggerOnSelectAll) {
                  this.options.onSelectAll(selected);
              }
          },

          /**
           * Deselects all options.
           *
           * If justVisible is true or not specified, only visible options are deselected.
           *
           * @param {Boolean} justVisible
           */
          deselectAll: function (justVisible, triggerOnDeselectAll) {
              if (!this.options.multiple) {
                  // In single selection mode at least on option needs to be selected
                  return;
              }

              // Record changes, i.e., those options that are deselected but were not deselected before.
              var deselected = [];
              var justVisible = typeof justVisible === 'undefined' ? true : justVisible;

              if (justVisible) {
                  var visibleOptions = $(".multiselect-option:not(.disabled):not(.multiselect-filter-hidden)", this.$popupContainer);
                  $('input[type="checkbox"]:enabled', visibleOptions).prop('checked', false);
                  visibleOptions.removeClass(this.options.selectedClass);

                  $('input[type="checkbox"]:enabled', visibleOptions).each($.proxy(function (index, element) {
                      var id = $(element).attr('id');
                      var option = this.getOptionById(id);
                      if ($(option).prop('selected')) {
                          deselected.push(option);
                      }
                      $(option).prop('selected', false);
                  }, this));
              }
              else {
                  var allOptions = $(".multiselect-option:not(.disabled):not(.multiselect-group)", this.$popupContainer);
                  $('input[type="checkbox"]:enabled', allOptions).prop('checked', false);
                  allOptions.removeClass(this.options.selectedClass);

                  $('input[type="checkbox"]:enabled', allOptions).each($.proxy(function (index, element) {
                      var id = $(element).attr('id');
                      var option = this.getOptionById(id);
                      if ($(option).prop('selected')) {
                          deselected.push(option);
                      }
                      $(option).prop('selected', false);
                  }, this));
              }

              $('.multiselect-all input[value="' + this.options.selectAllValue + '"]', this.$popupContainer).prop('checked', false);

              if (this.options.enableClickableOptGroups && this.options.multiple) {
                  this.updateOptGroups();
              }

              this.updateButtonText();
              this.updateSelectAll();

              if (triggerOnDeselectAll) {
                  this.options.onDeselectAll(deselected);
              }
          },

          /**
           * Rebuild the plugin.
           *
           * Rebuilds the dropdown, the filter and the select all option.
           */
          rebuild: function () {
              this.internalIdCount = 0;

              this.$popupContainer.html('');
              this.$select.find('option, optgroup').removeAttr('data-multiselectid');

              // Important to distinguish between radios and checkboxes.
              this.options.multiple = this.$select.attr('multiple') === "multiple";

              this.buildSelectAll();
              this.buildDropdownOptions();
              this.buildFilter();
              this.buildButtons();

              this.updateButtonText();
              this.updateSelectAll(true);

              if (this.options.enableClickableOptGroups && this.options.multiple) {
                  this.updateOptGroups();
              }

              if (this.options.disableIfEmpty) {
                  if ($('option', this.$select).length <= 0) {
                      if (!this.$select.prop('disabled')) {
                          this.disable(true);
                      }
                  }
                  else if (this.$select.data("disabled-by-option")) {
                      this.enable();
                  }
              }

              if (this.options.dropRight) {
                  this.$container.addClass('dropright');
              }
              else if (this.options.dropUp) {
                  this.$container.addClass('dropup');
              }

              if (this.options.widthSynchronizationMode !== 'never') {
                  this.synchronizeButtonAndPopupWidth();
              }
          },

          /**
           * The provided data will be used to build the dropdown.
           */
          dataprovider: function (dataprovider) {

              var groupCounter = 0;
              var $select = this.$select.empty();

              $.each(dataprovider, function (index, option) {
                  var $tag;

                  if ($.isArray(option.children)) { // create optiongroup tag
                      groupCounter++;

                      $tag = $('<optgroup/>').attr({
                          label: option.label || 'Group ' + groupCounter,
                          disabled: !!option.disabled,
                          value: option.value
                      });

                      forEach(option.children, function (subOption) { // add children option tags
                          var attributes = {
                              value: subOption.value,
                              label: subOption.label !== undefined && subOption.label !== null ? subOption.label : subOption.value,
                              title: subOption.title,
                              class: subOption.class,
                              selected: !!subOption.selected,
                              disabled: !!subOption.disabled
                          };

                          //Loop through attributes object and add key-value for each attribute
                          for (var key in subOption.attributes) {
                              attributes['data-' + key] = subOption.attributes[key];
                          }
                          //Append original attributes + new data attributes to option
                          $tag.append($('<option/>').attr(attributes));
                      });
                  }
                  else {
                      var attributes = {
                          'value': option.value,
                          'label': option.label !== undefined && option.label !== null ? option.label : option.value,
                          'title': option.title,
                          'class': option['class'],
                          'selected': !!option['selected'],
                          'disabled': !!option['disabled']
                      };
                      //Loop through attributes object and add key-value for each attribute
                      for (var key in option.attributes) {
                          attributes['data-' + key] = option.attributes[key];
                      }
                      //Append original attributes + new data attributes to option
                      $tag = $('<option/>').attr(attributes);

                      $tag.text(option.label !== undefined && option.label !== null ? option.label : option.value);
                  }

                  $select.append($tag);
              });

              this.rebuild();
          },

          /**
           * Enable the multiselect.
           */
          enable: function () {
              this.$select.prop('disabled', false);
              this.$button.prop('disabled', false)
                  .removeClass('disabled');

              this.updateButtonText();
          },

          /**
           * Disable the multiselect.
           */
          disable: function (disableByOption) {
              this.$select.prop('disabled', true);
              this.$button.prop('disabled', true)
                  .addClass('disabled');

              if (disableByOption) {
                  this.$select.data("disabled-by-option", true);
              }
              else {
                  this.$select.data("disabled-by-option", null);
              }

              this.updateButtonText();
          },

          /**
           * Set the options.
           *
           * @param {Array} options
           */
          setOptions: function (options) {
              this.options = this.mergeOptions(options);
          },

          /**
           * Merges the given options with the default options.
           *
           * @param {Array} options
           * @returns {Array}
           */
          mergeOptions: function (options) {
              return $.extend(true, {}, this.defaults, this.options, options);
          },

          /**
           * Checks whether a select all checkbox is present.
           *
           * @returns {Boolean}
           */
          hasSelectAll: function () {
              return $('.multiselect-all', this.$popupContainer).length > 0;
          },

          /**
           * Update opt groups.
           */
          updateOptGroups: function () {
              var $groups = $('.multiselect-group', this.$popupContainer)
              var selectedClass = this.options.selectedClass;

              $groups.each(function () {
                  var $options = $(this).nextUntil('.multiselect-group')
                      .not('.multiselect-filter-hidden')
                      .not('.disabled');

                  var checked = true;
                  $options.each(function () {
                      var $input = $('input', this);

                      if (!$input.prop('checked')) {
                          checked = false;
                      }
                  });

                  if (selectedClass) {
                      if (checked) {
                          $(this).addClass(selectedClass);
                      }
                      else {
                          $(this).removeClass(selectedClass);
                      }
                  }

                  $('input', this).prop('checked', checked);
              });
          },

          /**
           * Updates the select all checkbox based on the currently displayed and selected checkboxes.
           */
          updateSelectAll: function (notTriggerOnSelectAll) {
              if (this.hasSelectAll()) {
                  var allBoxes = $(".multiselect-option:not(.multiselect-filter-hidden):not(.multiselect-group):not(.disabled) input:enabled", this.$popupContainer);
                  var allBoxesLength = allBoxes.length;
                  var checkedBoxesLength = allBoxes.filter(":checked").length;
                  var selectAllItem = $(".multiselect-all", this.$popupContainer);
                  var selectAllInput = selectAllItem.find("input");

                  if (checkedBoxesLength > 0 && checkedBoxesLength === allBoxesLength) {
                      selectAllInput.prop("checked", true);
                      selectAllItem.addClass(this.options.selectedClass);
                  }
                  else {
                      selectAllInput.prop("checked", false);
                      selectAllItem.removeClass(this.options.selectedClass);
                  }
              }
          },

          /**
           * Update the button text and its title based on the currently selected options.
           */
          updateButtonText: function () {
              var options = this.getSelected();

              // First update the displayed button text.
              if (this.options.enableHTML) {
                  $('.multiselect .multiselect-selected-text', this.$container).html(this.options.buttonText(options, this.$select));
              }
              else {
                  $('.multiselect .multiselect-selected-text', this.$container).text(this.options.buttonText(options, this.$select));
              }

              // Now update the title attribute of the button.
              $('.multiselect', this.$container).attr('title', this.options.buttonTitle(options, this.$select));
              this.$button.trigger('change');
          },

          /**
           * Get all selected options.
           *
           * @returns {jQUery}
           */
          getSelected: function () {
              return $('option', this.$select).filter(":selected");
          },

          /**
           * Gets a select option by its id
           * @param {String} id
           * @returns {JQuery}
           */
          getOptionById: function (id) {
              if (!id) {
                  return null;
              }

              return this.$select.find('option[data-multiselectid=' + id + '], optgroup[data-multiselectid=' + id + ']');
          },

          /**
           * Get the input (radio/checkbox) by its value.
           *
           * @param {String} value
           * @returns {jQuery}
           */
          getInputsByValue: function (value) {
              var checkboxes = $('.multiselect-option input:not(.multiselect-search)', this.$popupContainer);
              var valueToCompare = value.toString();

              var matchingCheckboxes = [];
              for (var i = 0; i < checkboxes.length; i = i + 1) {
                  var checkbox = checkboxes[i];
                  if (checkbox.value === valueToCompare) {
                      matchingCheckboxes.push($(checkbox));
                  }
              }

              return matchingCheckboxes;
          },

          /**
           * Used for knockout integration.
           */
          updateOriginalOptions: function () {
              this.originalOptions = this.$select.clone()[0].options;
          },

          asyncFunction: function (callback, timeout, self) {
              var args = Array.prototype.slice.call(arguments, 3);
              return setTimeout(function () {
                  callback.apply(self || window, args);
              }, timeout);
          },

          setAllSelectedText: function (allSelectedText) {
              this.options.allSelectedText = allSelectedText;
              this.updateButtonText();
          },

          isFirefox: function () {
              var firefoxIdentifier = 'firefox';
              var valueNotFoundIndex = -1;

              if (navigator && navigator.userAgent) {
                  return navigator.userAgent.toLocaleLowerCase().indexOf(firefoxIdentifier) > valueNotFoundIndex;
              }

              return false;
          },

          /**
           * Generate a unique identifier inside the multiselect namespace and adds it as an data attribute to the related element
           * @param {JQuery} $relatedElement
           * @returns unique id
           */
          createAndApplyUniqueId: function ($relatedElement) {
              var id = 'multiselect_' + this.multiselectId + '_' + this.internalIdCount++;
              if (!!$relatedElement) {
                  $relatedElement[0].dataset.multiselectid = id;
              }
              return id;
          },

          /**
           * Generate a unique identifier
           * @returns unique id
           */
          generateUniqueId: function() {
              return Math.random().toString(36).substr(2);
          }
      };

      $.fn.multiselect = function (option, parameter, extraOptions) {
          return this.each(function () {
              var data = $(this).data('multiselect');
              var options = typeof option === 'object' && option;

              // Initialize the multiselect.
              if (!data) {
                  data = new Multiselect(this, options);
              }

              // Call multiselect method.
              if (typeof option === 'string') {
                  data[option](parameter, extraOptions);
              }
          });
      };

      $.fn.multiselect.Constructor = Multiselect;

      $(function () {
          $("select[data-role=multiselect]").multiselect();
      });

  });



// variable that keeps all the filter information
var send_data = {}


$(document).ready(function () {
    // reset all parameters on page load
    console.log('hello there');
    resetFilters();
    // bring all the data without any filters
    console.log('hello there 2');
    getAPIData();
    // get all countries from database via
    console.log('hello there 3');
    // AJAX call into country select options

    //getBackground();
    // get all varities from database via
    console.log('hello there 4');
    // AJAX call into variert select options

    getMatching();
    getCollections();
    console.log('hello there 5');
    // on selecting the country option
    console.log('hello there 6');
    $('#background').on('change', function () {
        // since province and region is dependent

        // on country select, empty all the options from select input

        $("#title").val("all");
        $("#ownerWallet").val("all");
        send_data['title'] = '';
        send_data['ownerWallet'] = '';

        // update the selected country
        console.log('this is what on click backghround sends');
        console.log(this.value)
        console.log(typeof this.value)
        var values = $('#background').val();
        console.log(values);
        console.log(typeof values);
        let l = []
        for (var v in values) {
          l.push(values[v]);
        }
        send_data['background'] = l;
        //   send_data['background'] += values[v];
        // }
        // if(this.value == "all")
        //     send_data['background'] = "";
        // else
        //     send_data['background'] = this.value;

        //get province of selected country
        console.log('right here send data stuff');
        console.log(send_data);
        // get api data of updated filters


        getAPIData();

    });

    function onChange(specific_category_name, base_category, parent=false, parent_key=false) {
      var values = $('#' + specific_category_name).val();
      let l = [];
      for (var v in values) {
        l.push(values[v]);
      }
      if (parent) {
        console.log('default worked');
        console.log(parent)
        var chk = $("input[type='checkbox'][value=" + parent + "]");
        console.log(chk);
        chk.prop("checked", true);

        var values = $('#' + parent_key).val();
        console.log(values);
        console.log(typeof values);
        let l = []
        for (var v in values) {
          l.push(values[v]);
        }
        send_data[parent_key] = l
      }

      send_data[base_category] = l;
      // get api data of updated filters
      getAPIData();
    }

    $('#background_specific_atmospheric').on('change', function () {
      onChange('background_specific_atmospheric', 'background_specific', 'Atmospheric', 'background');
    });
    $('#background_specific_colors').on('change', function () {
      onChange('background_specific_colors', 'background_specific', 'Colors', 'background');
    });
    $('#background_specific_dimensions').on('change', function () {
      onChange('background_specific_dimensions', 'background_specific', 'Dimensions', 'background');
    });



    // on filtering the variety input

    $('#fur').on('change', function () {
        // get the api data of updated variety
        var values = $('#fur').val();
        console.log(values);
        console.log("the above")
        let l = []
        for (var v in values) {
          l.push(values[v]);
        }
        send_data['fur'] = l;
        getAPIData();
    });

    $('#fur_specific').on('change', function () {
        // get the api data of updated variety
        var values = $('#fur_specific').val();
        let l = []
        for (var v in values) {
          l.push(values[v]);
        }
        send_data['fur_specific'] = l;
        getAPIData();
    });


    $('#swag').on('change', function () {
        // get the api data of updated variety
        var values = $('#swag').val();
        let l = []
        for (var v in values) {
          l.push(values[v]);
        }
        send_data['swag'] = l;
        getAPIData();
    });

    $('#swag_specific').on('change', function () {
        // get the api data of updated variety
        var values = $('#swag_specific').val();
        let l = []
        for (var v in values) {
          l.push(values[v]);
        }
        send_data['swag_specific'] = l;
        getAPIData();
    });

    $('#horns').on('change', function () {
        // get the api data of updated variety

        if(this.value == "all")
            send_data['horns'] = "";
        else
            send_data['horns'] = this.value;
        getAPIData();
    });

    $('#eyes').on('change', function () {
        // get the api data of updated variety

        if(this.value == "all")
            send_data['eyes'] = "";
        else
            send_data['eyes'] = this.value;
        getAPIData();
    });

    $('#mouth').on('change', function () {
        // get the api data of updated variety

        if(this.value == "all")
            send_data['mouth'] = "";
        else
            send_data['mouth'] = this.value;
        getAPIData();
    });

    $('#matching').on('change', function () {
        // get the api data of updated variety

        if(this.value == "all")
            send_data['matching'] = "";
        else
            send_data['matching'] = this.value;
        getAPIData();
    });

    $('#collections').on('change', function () {
        // get the api data of updated variety

        if(this.value == "all")
            send_data['collections'] = "";
        else
            send_data['collections'] = this.value;
        getAPIData();
    });
    // on filtering the province input

    $('#title').on('change', function () {
        // clear the region input

        // since it is dependent on province input

        send_data['ownerWallet'] = "";
        $('#ownerWallet').val("all");
        if(this.value == "all")
            send_data['title'] = "";
        else
            send_data['title'] = this.value;
        getAPIData();
    });

    // on filtering the region input

    $('#ownerWallet').on('change', function () {
        if(this.value == "all")
            send_data['ownerWallet'] = "";
        else
            send_data['ownerWallet'] = this.value;
        getAPIData();
    });

    // sort the data according to price/points

    $('#sort_by').on('change', function () {
        send_data['sort_by'] = this.value;
        getAPIData();
    });

    // display the results after reseting the filters

    $("#display_all").click(function(){
        resetFilters();
        getAPIData();
    })
    $("#background_feature").click(function(){
      console.log('oh have th turns tbaled');
      })
})


/**
    Function that resets all the filters
**/
function addLeadingZeros(num, totalLength) {
  return String(num).padStart(totalLength, '0');
}

function resetFilters() {
    console.log('reset filters')
    $("#background").val("all");
    $("#background_specific").val("all");
    $("#fur").val("all");
    $("#fur_specific").val("all");
    $("#swag").val("all");
    $("#swag_specific").val("all");
    $("#horns").val("all");
    $("#eyes").val("all");
    $("#mouth").val("all");
    $("#matching").val("all");
    $("#collections").val("all");
    $("#title").val("all");
    $("#ownerWallet").val("all");
    $("#sort_by").val("none");

    //clearing up the province and region select box


    send_data['background'] = '';
    send_data['background_specific'] = '';
    send_data['fur'] = '';
    send_data['fur_specific'] = '';
    send_data['swag'] = '';
    send_data['swag_specific'] = '';
    send_data['horns'] = '';
    send_data['eyes'] = '';
    send_data['mouth'] = '';
    send_data['matching'] = '';
    send_data['collections'] = '';
    send_data['title'] = '';
    send_data['ownerWallet'] = '';
    send_data["sort_by"] = '',
    send_data['format'] = 'json';
}

/**.
    Utility function to showcase the api data
    we got from backend to the table content
**/

function putTableData(result) {
    // creating table row for each result and

    // pushing to the html cntent of table body of listing table

    let row;
    if(result["results"].length > 0){
        console.log('pit swtop');
        $("#no_results").hide();
        $("#list_data").show();
        $("#listing").html("");
        $("#listing").append(row);

        $.each(result["results"], function (a, b) {
            let title;
            if (b.title != null) {
              title = " - " + b.title
            }
            else {
              title = ""
            }
            if (b.uniqueId <= 9910) {
              let smoking;
              let double_baby_buff;
              let matching;
              let collections;

              if (b.traits.smoking != "N/A") {
                smoking = "<td>" + b.traits.smoking_rarity + "%</td>"
              }
              else {
                smoking = "<td>" + b.traits.smoking_rarity + "</td>"
              }
              if (b.traits.double_baby_buff_rarity != "N/A") {
                double_baby_buff = "<td>" + b.traits.double_baby_buff_rarity + "%</td>"
              }
              else {
                double_baby_buff = "<td>" + b.traits.double_baby_buff_rarity + "</td>"
              }
              if (b.traits.matching_buff_score > 0) {
                dic_string = b.traits.matching_dictionary
                console.log('we right ehre do')
                d = JSON.parse(dic_string)
                for (var key in d) {
                  matching += "<tr> \
                    <th scope='row'>Matching</th> \
                    <td>" + key + "</td> \
                    <td>" + d[key][0] + " matches</td> \
                    <td>N/A</td> \
                    <td>" + d[key][2] + "</td> \
                  </tr> "
                }
              }
              else {
                matching = "<tr> \
                  <th scope='row'>Matching</th> \
                  <td>No</td> \
                  <td>N/A</td> \
                  <td>N/A</td> \
                  <td>0</td> \
                </tr>"
              }
              if (b.traits.collections_dictionary != "No") {
                dic_string = b.traits.collections_dictionary
                d = JSON.parse(dic_string)
                for (var key in d) {
                  collections += "<tr> \
                                  <th scope='row'>Collection</th> \
                                  <td>" + d[key][0] + "</td> \
                                  <td>" + d[key][1] + "</td> \
                                  <td>" + d[key][2] + "%</td> \
                                  <td>" + d[key][3] + "</td> \
                                </tr>"
                }
              }
              else {
                collections = "<tr> \
                                <th scope='row'>Collection</th> \
                                <td>No</td> \
                                <td>N/A</td> \
                                <td>N/A</td> \
                                <td>0</td> \
                              </tr>"
              }

              row = "<div class='col'> \
                  <div class='card-full shadow-sm'> \
                    <div class='card'> \
                      <div class='face front card-img'> \
                        <img class='card-img' src=" + b.img_url + " alt='Buff Wild Crew NFT Card Front'> \
                      </div> \
                      <div class='face back card-img'> \
                        <img class='card-img' src='https://buffwild.b-cdn.net/SiteImages/Buff_Wild_Card_Back.png' alt='Buff Wild Crew NFT Card Back'> \
                        <div class='card-img-overlay'> \
                          <p-num class='card-title'>#" + addLeadingZeros(b.uniqueId, 4) + "</p-num> \
                          <div class='table-responsive'> \
                            <div class='container py-1'> \
                            <table class='table table-bordered table-hover table-sm'> \
                            <thead class='thead-light'> \
                              <tr> \
                                <th scope='col'>Category</th> \
                                <th scope='col'>Feature</th> \
                                <th scope='col'>Specific</th> \
                                <th scope='col'>Rarity</th> \
                                <th scope='col'>Score</th> \
                              </tr> \
                            </thead> \
                            <tbody> \
                              <tr> \
                                <th scope='row'>Background</th> \
                                <td>" + b.traits.background_feature + "</td> \
                                <td>" + b.traits.background_specific + "</td> \
                                <td>" + b.traits.background_feature_rarity + "%</td> \
                                <td>" + b.traits.background_buff_score + "</td> \
                              </tr> \
                              <tr> \
                                <th scope='row'>Fur</th> \
                                <td>" + b.traits.fur_feature + "</td> \
                                <td>" + b.traits.fur_specific + "</td> \
                                <td>" + b.traits.fur_feature_rarity + "%</td> \
                                <td>" + b.traits.fur_buff_score + "</td> \
                              </tr> \
                              <tr> \
                                <th scope='row'>Eyes</th> \
                                <td>" + b.traits.eyes_feature + "</td> \
                                <td>" + b.traits.eyes_specific + "</td> \
                                <td>" + b.traits.eyes_feature_rarity + "%</td> \
                                <td>" + b.traits.eyes_buff_score + "</td> \
                              </tr> \
                               <tr> \
                                <th scope='row'>Mouth</th> \
                                <td>" + b.traits.mouth_feature + "</td> \
                                <td>" + b.traits.mouth_specific + "</td> \
                                <td>" + b.traits.mouth_feature_rarity + "%</td> \
                                <td>" + b.traits.mouth_buff_score + "</td> \
                              </tr> \
                              <tr> \
                                <th scope='row'>Horns</th> \
                                <td>" + b.traits.horns_feature + "</td> \
                                <td>" + b.traits.horns_specific + "</td> \
                                <td>" + b.traits.horns_feature_rarity + "%</td> \
                                <td>" + b.traits.horns_buff_score + "</td> \
                              </tr> \
                              <tr> \
                                <th scope='row'>Swag</th> \
                                <td>" + b.traits.swag_feature + "</td> \
                                <td>" + b.traits.swag_specific + "</td> \
                                <td>" + b.traits.swag_feature_rarity + "%</td> \
                                <td>" + b.traits.swag_buff_score + "</td> \
                              </tr> \
                              <tr> \
                                <th scope='row'>Smoking</th> \
                                <td>" + b.traits.smoking + "</td> \
                                <td>N/A</td>" + smoking +
                                "<td>" + b.traits.smoking_buff_score + "</td> \
                              </tr> \
                              <tr> \
                                <th scope='row'>Double Baby</th> \
                                <td>" + b.traits.double_baby_buff + "</td> \
                                <td>N/A</td>" + double_baby_buff +
                                "<td>" + b.traits.double_baby_buff_buff_score + "</td> \
                              </tr>" + matching + collections +
                            "</tbody> \
                            </table> \
                            </div> \
                            </div> \
                            <p-score class='card-title'>Buff Score: " + b.traits.total_buff_score + "</p-score> \
                          </div> \
                        </div> \
                      </div> \
                      <div class='container buff-info'> \
                      <a style='text-align:center; color:#FFFFFF; background-color:#000000;'> \
                        <p style='text-align:center; color:#FFFFFF; background-color:#000000;'> \
                          #" + b.uniqueId + title +
                        "<div class='row traderow'> \
                          <div class='col-4 trade buy rounded-pill'> \
                            B" + b.tradeId + " \
                          </div> \
                          <div class='col-4 trade sell rounded-pill'> \
                            S" + b.tradeId + " \
                          </div> \
                          <div class='col-4 trade cancel rounded-pill'> \
                            C" + b.tradeId + " \
                          </div> \
                        </div> \
                        <p style='text-align:center; color:#FFFFFF; background-color:#000000;'> \
                          Price: " + b.forSale + " XRD </p> \
                    </a> \
                    </div> \
                  </div> \
                </div>"
            }
            else {
              row = "<div class='col'> \
                        <div class='card-full shadow-sm'> \
                          <div class='card'> \
                              <img class='card-img' src=" + b.img_url + " alt='Buff Wild Crew NFT Card Front'> \
                          </div> \
                          <div class='container buff-info'> \
                          <a style='text-align:center; color:#FFFFFF; background-color:#000000;'> \
                            <p style='text-align:center; color:#FFFFFF; background-color:#000000;'> \
                            #" + b.uniqueId + title +
                            "<div class='row traderow'> \
                              <div class='col-4 trade buy rounded-pill'> \
                                B" + b.tradeId + " \
                              </div> \
                              <div class='col-4 trade sell rounded-pill'> \
                                S" + b.tradeId + " \
                              </div> \
                              <div class='col-4 trade cancel rounded-pill'> \
                                C" + b.tradeId + " \
                              </div> \
                            </div> \
                            <p style='text-align:center; color:#FFFFFF; background-color:#000000;'> \
                              Price: " + b.forSale + " XRD </p> \
                        </a> \
                      </div> \
                      </div> \
                </div>"
            }

            $("#listing").append(row);
        });
        const card = document.querySelectorAll('.card');
        // Loop through cards.
        // This is so you can have multiple cards on a page.
        for (let i = 0; i < card.length; i++) {
           // Add a click event listener to each card.
           card[i].addEventListener("click", function() {
             // Toggle active class on card
             card[i].classList.toggle("flip");
           });
        }
    }
    else{
        // if no result found for the given filter, then display no result

        $("#no_results h5").html("No results found");
        $("#list_data").hide();
        $("#no_results").show();
    }
    // setting previous and next page url for the given result

    let prev_url = result["previous"];
    let next_url = result["next"];
    // disabling-enabling button depending on existence of next/prev page.

    if (prev_url === null) {
        $("#previous").addClass("disabled");
        $("#previous").prop('disabled', true);
    } else {
        $("#previous").removeClass("disabled");
        $("#previous").prop('disabled', false);
    }
    if (next_url === null) {
        $("#next").addClass("disabled");
        $("#next").prop('disabled', true);
    } else {
        $("#next").removeClass("disabled");
        $("#next").prop('disabled', false);
    }
    // setting the url

    $("#previous").attr("url", result["previous"]);
    $("#next").attr("url", result["next"]);
    // displaying result count

    $("#result-count span").html(result["count"]);
    console.log('now its done')
}

function getAPIData() {
    console.log('start get api data')
    console.log(send_data)
    let url = $('#list_data').attr("url")
    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        beforeSend: function(){
            $("#no_results h5").html("Loading data...");
        },
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            $("#no_results h5").html("Something went wrong");
            $("#list_data").hide();
        }
    });
    console.log('end get api data')
}

function getMatching() {
    // fill the options of varities by making ajax call

    // obtain the url from the varities select input attribute

    let url = $("#matching").attr("url");
    // makes request to getvariety(request) method in views
    console.log('hi im matching');
    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {

            matching_options = "<option value='all' selected>All Colors</option>";
            $.each(result["matching"], function (a, b) {
                matching_options += "<option>" + b + "</option>"
            });
            $("#matching").html(matching_options)
        },
        error: function(response){
            console.log(response)
        }
    });
}

function getCollections() {
    // fill the options of varities by making ajax call

    // obtain the url from the varities select input attribute

    let url = $("#collections").attr("url");
    // makes request to getvariety(request) method in views
    console.log('hi im matching');
    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {

            collections_options = "<option value='all' selected>All Collections</option>";
            $.each(result["collections"], function (a, b) {
                collections_options += "<option>" + b + "</option>"
            });
            $("#collections").html(collections_options)
        },
        error: function(response){
            console.log(response)
        }
    });
}


$("#next").click(function () {
    // load the next page data and

    // put the result to the table body

    // by making ajax call to next available url

    let url = $(this).attr("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function(response){
            console.log(response)
        }
    });
})

$("#previous").click(function () {
    // load the previous page data and

    // put the result to the table body

    // by making ajax call to previous available url

    let url = $(this).attr("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function(response){
            console.log(response)
        }
    });
})
$(function () {
  $('select[data-toggle="collapse"]').on('click',function(){

    var objectID=$(this).attr('href');

    if($(objectID).hasClass('in'))
    {
      $(objectID).collapse('hide');
    }

    else{
      $(objectID).collapse('show');
    }
  });


});
function hello() {
console.log('THE FUNCTION RAN');
}
var el = document.getElementById('background_feature');
if (el) {
  el.addEventListener('click', hello);
}

$('#background_feature').click(function () {
    // get the api data of updated variety
    console.log('we hit it it works it owkrs it works');
    var values = $('#fur').val();
    console.log(values);
    console.log("the above")
    let l = []
    for (var v in values) {
      l.push(values[v]);
    }
    send_data['fur'] = l;
    getAPIData();
});

</script>


<!-- Initialize the plugin: -->
<script type="text/javascript">
    $(document).ready(function() {
        $('#background').multiselect();
    });
    $(document).ready(function() {
        $('#background_specific_atmospheric').multiselect();
    });
    $(document).ready(function() {
        $('#background_specific_colors').multiselect();
    });
    $(document).ready(function() {
        $('#background_specific_dimensions').multiselect();
    });
    $(document).ready(function() {
        $('#fur').multiselect();
    });
    $(document).ready(function() {
        $('#fur_specific').multiselect();
    });
    $(document).ready(function() {
        $('#swag').multiselect();
    });
    $(document).ready(function() {
        $('#swag_specific').multiselect();
    });

</script>

</head>
<body>
  <div class="container logocontainer">
  <img src="https://buffwild.b-cdn.net/SiteImages/logo_banner.png" alt="Buff Wild Crew Logo Banner"/>
  </div>
<main>
<div class="cover-container d-inline-flex h-100 w-100 p-3 mt-2 mb-0 mx-auto flex-column">
  <section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1 class="fw-light">Buffs for Sale</h1>
        <p class="lead text-muted"></p>
        <div class="row row-cols-1 row-cols-md-3 g-3 gy-3 buttonrow">
          <div class="col buffbutton">
            <a href="{% url 'walletLookup' %}" class="btn btn-lg btn-block" role="button">My Buffs</a>
          </div>
          <div class="col buffbutton">
            <a href="{% url 'collection' %}" class="btn btn-info btn-lg btn-block" role="button">Collection</a>
          </div>
          <div class="col buffbutton">
            <a href="{% url 'chest' %}" class="btn btn-lg btn-block" role="button">Faction Chest</a>
          </div>
        </div>
    </div>
  </section>

  <div class="col text-center">
    <div class="row text-center">
      <h2>TRADING INSTRUCTIONS</h2>
    </div>

    <div class="row text-center">
      <p1>WALLET</p1>
      <p>The wallet is rdx1qsp0ez9yxa0l5qwf6fz93tda6842fft3cqr44ak3mgjtn9p4eme8wrccm4922 (The same as the minting wallet)</p>
      <p1>SELLING</p1>
      <p>The minimum sales price is 50 xrd. To sell your buff send the appropriate token to our wallet along with the <span style="color: #EEDC5B">sell code</span> and your asking price as the message, like this <span style="color: #EEDC5B">S439PGU</span>-500 to sell for 500 XRD. All sales are subject to a 10% royalty</p>
      <p1>BUYING</p1>
      <p>To buy a buff, simply send the amount of xrd the seller is requesting to our wallet along with the <span style="color: #0000FF">buy code</span> as the message</p>
      <p1>TO CANCEL A SALES LISTING</p1>
      <p>If you would like to cancel your listing send 3 xrd to the wallet along with the <span style="color: #FF0000">cancel code</span> as the message</p>
      <p1>SEQUESTERED TOKENS</p1>
      <p>your token will be sequestered if:</p>
      <p>-You sent a buff token when you should’ve sent a buff1 token, or visa versa</p>
      <p>-You try to sell someone elses buff</p>
      <p>-You have a buff currently listed for sale and try to list it for sale again without cancelling first</p>
      <p>-You try to sell for below the minimum sales price</p>
      <p>-You try to send a sales price with too many decimal places, we accept 6 decimal places max</p>
      <p>-You send an invalid sales price (we only accept numbers)</p>
      <p1>Rescuing a sequestered token</p1>
      <p>To rescue a sequestered token send 3 xrd to the wallet along with SOS as the message</p>
      <br>
      <br>
    </div>

  </div>

  <div class="big-box container-fluid">
    <div class="container-fluid">
      <div class="row">
        <div class="col-3">
          <div class="row">
    <section class="site_filter">
        <div class="row">
          <div class="col-12">
            <div class="background_box">
              <button type="button" class="btn-block collapsible-link collapsed" data-toggle="collapse" data-target="#Background">Background</button>
              <div id="Background" class="trait-category collapse">
                <div class="row trait-feature-row">
                  <div class="col-6">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" value="Atmospheric" id="background_feature" name="background_feature">
                  <label class="form-check-label" for="flexCheckDefault">
                    Atmospheric
                  </label>
                </div>
                </div>
                <div class="col-6">
                  <div class="col-sm-2 col-2">
                    <select id="background_specific_atmospheric" multiple="multiple">
                  <option value="Starry Night">Starry Night</option>
                  <option value="Towards the Storm">Towards the Storm</option>
                  <option value="Tornado">Tornado</option>
                  <option value="Highlands">Highlands</option>
                  <option value="Graveyard">Graveyard</option>
                  <option value="Alien World">Alien World</option>
                </select>
            </div>
                </div>
                </div>
                <div class="row trait-feature-row">
                  <div class="col-6">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" value="Colors" id="background_feature" name="background_feature">
                  <label class="form-check-label" for="tester">
                    Colors
                  </label>
                </div>
                </div>
                <div class="col-6">
                  <div class="col-sm-2 col-2">
                    <select id="background_specific_colors" multiple="multiple">
                        <option value="Desert Yellow">Desert Yellow</option>
                        <option value="Green">Green</option>
                        <option value="Grey">Grey</option>
                        <option value="Gue Pink">Gue Pink</option>
                        <option value="Ice Blue">Ice Blue</option>
                        <option value="Purple">Purple</option>
                        <option value="Red">Red</option>
                      </select>
                </div>
                </div>
                </div>
                <div class="row trait-feature-row">
                  <div class="col-6">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" value="Dimensions" id="background_feature"  name="background_feature">
                  <label class="form-check-label" for="flexCheckDefault">
                    Dimensions
                  </label>
                </div>
                </div>
              <div class="col-6">
                <div class="col-sm-2 col-2">
                  <select id="background_specific_dimensions" multiple="multiple">
                      <option value="Heaven">Heaven</option>
                      <option value="Hellfire">Hellfire</option>
                      <option value="Trippy">Trippy</option>
                      <option value="Matrix">Matrix</option>
                    </select>
                </div>
              </div>
              </div>
            </div>
          </div>
            <!-- <div class="col-sm-2 col-2">
              <label for="background">Background</label>
              <select data-toggle="collapse" id="background" multiple="multiple">
                  <option value="Atmospheric">Atmospheric</option>
                  <option value="Colors">Colors</option>
                  <option value="Dimensions">Dimensions</option>
                </select>
            </div> -->

            <div class="col-sm-2 col-2">
              <label for="fur">Fur</label>
              <select id="fur" multiple="multiple">
                  <option value="Standard">Standard</option>
                  <option value="Animal">Animal</option>
                  <option value="Designer">Designer</option>
                  <option value="The Risen">The Risen</option>
                  <option value="The Elders">The Elders</option>
                  <option value="The Demi Buff">The Demi Buff</option>
                  <option value="White Angel">White Angel</option>
                  <option value="Devilish">Devilish</option>
                </select>
            </div>
            <div class="col-sm-2 col-2">
              <label for="fur_specific">Fur Specific</label>
              <select id="fur_specific" multiple="multiple">
                <optgroup label="Standard">
                  <option value="Purple">Purple</option>
                  <option value="Base Buff">Base Buff</option>
                  <option value="Browny">Browny</option>
                  <option value="Ginger Snap">Ginger Snap</option>
                </optgroup>
                <optgroup label="Animal">
                  <option value="Black Leopard">Black Leopard</option>
                  <option value="Cheetah">Cheetah</option>
                  <option value="Cheetah Blue">Cheetah Blue</option>
                  <option value="Leopard Green">Leopard Green</option>
                </optgroup>
              </select>
            </div>
            <div class="col-sm-2 col-2">
              <label for="swag">Swag</label>
              <select id="swag" multiple="multiple">
                  <option value="Standard">Standard</option>
                  <option value="Middle Class Fancy">Middle Class Fancy</option>
                  <option value="Premium Swag">Premium Swag</option>
                  <option value="Baby Buff">Baby Buff</option>
                  <option value="Premium Ink">Premium Ink</option>
                  <option value="Premium Weapons">Premium Weapons</option>
                  <option value="Bane Veins">Bane Veins</option>
                  <option value="Symbol">Symbol</option>
                </select>
            </div>
            <div class="col-sm-2 col-2">
              <label for="swag_specific">Swag Specific</label>
              <select id="swag_specific" multiple="multiple">
                  <option value="Chadagonia Blue">Chadagonia Blue</option>
                  <option value="Chadagonia Yellow">Chadagonia Yellow</option>
                  <option value="Chadagonia Red">Chadagonia Red</option>
                  <option value="Chadagonia Green">Chadagonia Green</option>
                  <option value="Chadagonia Black">Chadagonia Black</option>
                  <option value="Ryan">Ryan</option>
                  <option value="Easter Morning">Easter Morning</option>
                  <option value="Super Hero">Super Hero</option>
                </select>
            </div>
            <div class="col-sm-2 col-2">
                <div class="form-group">
                    <label for="matching">Matching Colors</label>
                    <select class="form-control" id="matching"
                        url = "{%url 'main:get_matching' %}">
                    </select>
                </div>
            </div>
            <div class="col-sm-2 col-2">
                <div class="form-group">
                    <label for="collections">Collections</label>
                    <select class="form-control" id="collections"
                        url = "{%url 'main:get_collections' %}">
                    </select>
                </div>
            </div>
            <div class="col-sm-2 col-2">
              <select id="title" multiple="multiple">
                  <option value="cheese">Cheese</option>
                  <option value="tomatoes">Tomatoes</option>
                  <option value="mozarella">Mozzarella</option>
                  <option value="mushrooms">Mushrooms</option>
                  <option value="pepperoni">Pepperoni</option>
                  <option value="onions">Onions</option>
              </select>

            </div>

            <div class="col-sm-2 col-2">
                <div class="form-group">
                    <label for="sort_by">Sort By</label>
                    <select class="form-control" id="sort_by">
                        <option selected="true"
                        disabled="disabled" value = "none">Choose option</option>
                        <option value='uniqueId_ascending'>Mint Number: Low to High</option>
                        <option value='uniqueId_descending'>Mint Number: High to Low</option>
                        <option value='forSale_ascending'>Price: Low to High</option>
                        <option value='forSale_descending'>Price: High to Low</option>
                        <option value='buffScore_ascending'>Buff Score: Low to High</option>
                        <option value='buffScore_descending'>Buff Score: High to Low</option>
                    </select>
                </div>
            </div>
            <div class="col-sm-2 col-2">
                <div class="row justify-content-center align-self-center"
                    style="color:white; margin-top:30px;">
                    <a class="btn btn-secondary" id="display_all">Display all</a>
                </div>
            </div>
        </div>
      </section>
      </div>
    </div>

<div class="col-9">
<section>
    <div class="container-fluid">
        <div id = "result-count" class="text-right">
            <span class='font-weight-bold'></span> results found.
        </div>
        <div class="row properties_table justify-content-center">
            <div id = "no_results">
                <h5>No results found</h5>
            </div>
            <div class="album py-5">
              <div class="container-fluid buff-results" id="list_data" url = "{% url 'main:listing' %}">
                <div class="row row-cols-4 g-3" id="listing" data-toggle="table">
                </div>
              </div>
            </div>

        </div>
        <div class="row justify-content-center">
            <nav aria-label="navigation">
                <ul class="pagination">
                    <li class="page-item">
                        <button class="btn btn-primary page-link" id="previous">Previous</button>
                    </li>
                    <li class="page-item pull-right">
                        <button class="btn btn-primary page-link" id="next">Next</button>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</section>
</div>
</div>
</div>
</main>
<script>
  $(document).ready(function() {
      $('[name=background_feature]').click(function() {
        let l = []
        console.log('it was clicked yipee');
          $('input[name="background_feature"]').each(function() {    // $(':checkbox:checked')
            if ( $(this).is(':checked')) {
              console.log('yes it were')
              l.push(this.value);
            }              // $(this).val()
          });
        console.log('l is HERE');
        console.log(l);
        send_data['background'] = l;
        getAPIData();
      });
  });
</script>
</body>
{% endblock %}

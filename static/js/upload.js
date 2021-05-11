"use strict";

// wait until page is loaded
window.onload = init

// declare dom list
const dom = {}

function init() {
  // populate dom list
  dom.formItems = document.querySelector("#form_items")
  dom.itemAdd = document.querySelector("#item_add")
  dom.uploadSubmit = document.querySelector("#upload_submit")
  dom.uploadError = document.querySelector("#upload_error")

  dom.uploadName = document.querySelector("#upload_name")
  dom.uploadImage = document.querySelector("#upload_image")

  // add event listener for initial remove button
  const itemRemove = document.querySelector(".item_remove")
  itemRemove.addEventListener('click', removeItem)

  dom.itemAdd.addEventListener('click', addItem)

  dom.uploadSubmit.addEventListener('click', upload)
}

// add item to list
function addItem() {
  const domString = '<div class="form_item"><input class="upload_item" type="text" name="upload_item" placeholder="Item"><button class="item_remove">x</button></div>'
  
  // create temporary element
  const tempDiv = document.createElement('div')
  tempDiv.innerHTML = domString

  // add event listener for remove button
  const itemRemove = tempDiv.querySelector(".item_remove")
  itemRemove.addEventListener('click', removeItem)

  // append element to list
  dom.formItems.appendChild(tempDiv.firstChild)
}

// remove item from list
function removeItem() {
  this.parentElement.remove()
}

// upload new listing
function upload() {
  // verify each input is filled
  if (dom.uploadName.value == "" ||
    dom.uploadImage.value == "") {
      dom.uploadError.innerHTML = "Please complete all inputs."
      return
    }

  // create a FormData object for ajax requests
  const authForm = new FormData()

  // append information to form data
  authForm.append("name", dom.uploadName.value)
  authForm.append("image", dom.uploadImage.value)

  // create list of items
  const items = []
  const itemInputs = document.querySelectorAll(".upload_item")
  itemInputs.forEach((input) => {
    items.push(input.value)
  })
  console.log(items)

  // append list to form data
  authForm.append("items", items)

  // create a new ajax request
  const request = new XMLHttpRequest()

  // prepare to receive response
  request.addEventListener("readystatechange", handleResponse)

  // send request
  request.open("POST", "/upload")
  request.send(authForm)
}

function handleResponse() {
  if (this.readyState == 4) {
    // store request response
    const response = JSON.parse(this.response)

    if (response.status == 200) {
      location.reload()
    } else if (response.status == 401) {
      dom.uploadError.innerHTML = "Password is incorrect. Please try again."
    }
  }
}
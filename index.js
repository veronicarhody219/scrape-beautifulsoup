import data from "./img.json" assert {type: "json"};

console.log(data);

let imgsrc = Object.values(data.thumb);
let titles = Object.values(data.title);
let links = Object.values(data.link);
let ids = Object.keys(data.thumb);
const arrayOfArticles = ids.map((currentValue, index) => {
  return {
    id: currentValue,
    thumb: imgsrc[index],
    title: titles[index],
    link: links[index],
  };
});

console.log(imgsrc);
console.log(titles);
console.log(ids);
console.log(arrayOfArticles);

arrayOfArticles.map((item) => {
  let div = document.createElement("div");
  let para = document.createElement("p");
  let text = document.createTextNode(item.title);
  let img = document.createElement("img");
  let alink = document.createElement("a");
  img.setAttribute("src", item.thumb);
  img.setAttribute("alt", item.title);
  alink.setAttribute("href", item.link);
  alink.appendChild(text);
  para.appendChild(alink);
  document.body.appendChild(div);
  div.appendChild(img);
  div.appendChild(para);
});

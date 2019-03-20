percent계산

```html
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: {100*pick1/(pick1+pick2)}%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
</div>


```



투표

<div id="left-chart" class="progress-bar progress-bar-striped" role="progressbar" style="width: 23.3%;  background-color: #f14b4b;font-size: 14px;line-height: 30px;" aria-valuenow="23.3" aria-valuemin="0" aria-valuemax="100">23.3%</div>

<div id="right-chart" class="progress-bar progress-bar-striped bg-danger" role="progressbar" style="width: 76.7%; background-color: #315ec3;font-size: 14px;line-height: 30px;" aria-valuenow="76.7" aria-valuemin="0" aria-valuemax="100">76.7%</div>



```html
왼쪽
<div id="left-chart" class="progress-bar progress-bar-striped" role="progressbar" style="width: 23.3%;  background-color: #f14b4b;font-size: 14px;line-height: 30px;" aria-valuenow="23.3" aria-valuemin="0" aria-valuemax="100">23.3%</div>

오른쪽
<div id="right-chart" class="progress-bar progress-bar-striped bg-danger" role="progressbar" style="width: 76.7%; background-color: #315ec3;font-size: 14px;line-height: 30px;" aria-valuenow="76.7" aria-valuemin="0" aria-valuemax="100">76.7%</div>
```



선택 카드

```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
  </div>
</div>
```



Navbar

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Either</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">홈페이지 <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">새글</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">랜덤글</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
  </div>
</nav>
```
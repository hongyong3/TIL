# 20190704

## Vue



##### OPtimize_Chrome

* index.html의 <body> 아래에 추가한다.

```vue
<script>
  var userAgent = window.navigator.userAgent;
  var isChrome = userAgent.indexOf('Chrome');
  var isChromeMobile = userAgent.indexOf('CriOS');
  var isSamsungBrowser = userAgent.indexOf('SamsungBrowser');
  var isWindows = userAgent.indexOf('Windows NT');
  var isEdge = userAgent.indexOf('Edge');
  var isIE = userAgent.indexOf('Trident');

  // 크롬 브라우저 체크
  if(isChrome > -1 || isChromeMobile > -1){
      if(isSamsungBrowser < 0 && isEdge < 0){
    } else{
      alert("해당 사이트는 크롬에 최적화 되어 있습니다.")
    }
  } else{
    alert("해당 사이트는 크롬에 최적화 되어 있습니다.")
  }
  </script>
```


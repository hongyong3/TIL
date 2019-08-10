##### addWeeklyModal

```vue
<template>
    <div id="add-weekly-modal" class="modal-wrapper">
        <a href="#" class="modal-back"/>
        <div class="modal-box">
            <div class="modal-header">
                <span class="modal-title">주간 식단표 등록</span>
                <a href="#" class="modal-close">&times;</a>
            </div>
            <div class="modal-content">
                <div class="modal-info">
                    <!-- <input @change="test" id="file" ref="myfile" name="weekly-menu" type="file" class="filecontainer"/> -->
                    <input @change="getMenuData" id="menudata" type="file" class="filecontainer"/>
                    <button id="formButton" @click="sendData" class="form-button" disabled="" type="button">제출</button>
                </div>
            </div>
            <div class="modal-content2">
                <div class="modal-content2-title">
                    업로드된 식단표 미리보기
                </div>
                <div id="uploaded-menu">
                    <table>
                        <thead>
                            <tr>
                                <td></td>
                                <td>월</td>
                                <td>화</td>
                                <td>수</td>
                                <td>목</td>
                                <td>금</td>
                            </tr>
                            <tr id="menu-date"/>
                        </thead>
                        <tbody>
                            <tr id="menu-korean"/>
                            <tr id="menu-star"/>
                            <tr id="menu-special"/>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { eventBus } from '@/main'
// const testdata = require('./5thJul2019.json')

export default {
    name: "AddWeeklyMenuModal",
    props: [
        'date',
        'korean',
        'star',
        'special',
    ],
    data() {
        return {
            menudata: [],
        }
    },
    mounted() {

    },
    methods: {
        getMenuData() {
            const selectedFile = document.querySelector('#menudata').files[0]

            var reader = new FileReader()
            reader.onload = (e) => {
                this.menudata = JSON.parse(e.target.result)
                console.log('after parse', this.menudata)
                this.showMenuData(this.menudata)
            }
            reader.readAsText(selectedFile)
        },
        showMenuData(data) {
            this.getDataFromJson(data, "date", '#menu-date', '')
            this.getDataFromJson(data, "korean", '#menu-korean', '한식')
            this.getDataFromJson(data, "star", '#menu-star', '별식')
            this.getDataFromJson(data, "special", '#menu-special', '스페셜')
        },
        getDataFromJson(data, key, id, first) {
            let query = document.querySelector(id)
            for (let i = 0; i < 6; i++) {
                var cell = document.createElement('td')
                if (i == 0) {
                    var cellText = document.createTextNode(first)
                    cell.appendChild(cellText)
                    query.appendChild(cell)
                } else {
                    let keydata = data["menus"][i-1][key]
                    if (keydata.length) {
                        for (let j = 0; j < keydata.length; j++) {
                            var cellText = document.createTextNode(keydata[j])
                            cell.appendChild(cellText)
                            var br = document.createElement('br')
                            cell.appendChild(br)
                        }
                    } else {
                        var cellText = document.createTextNode(keydata)
                        cell.appendChild(cellText)
                    }
                    query.appendChild(cell)
                }
            }
        },
        sendData() {
            // eventBus 를 통해서 형제 컴포넌트에게 값을 전송할 수 있다.
            // eventBus가 하나의 부모 컴포넌트 역할을 하며  $emit를 통해서 신호를 받는다.
            // eventBus.$emit('userWasEdited', new Date()) 한개의 경우 전송 방법
            // main.js에 선언한 메소드로 전달
            eventBus.menuSended(new Date() )
        }
    },
}
</script>

<style lang="scss">
@import './AddWeeklyMenuModal.scss';
</style>

```



##### addWeeklyModalBro

```vue
<template>
<div>
  {{date}}
</div>
<div>
  {{korean}}
</div>
<div>
  {{star}}
</div>
<div>
  {{special}}
</div>
</template>

<script>
// const testdata = require('./5thJul2019.json')
import { eventBus } from '@/main'

export default {
    name: "AddWeeklyMenuModalBro",
    props: [
        'date',
        'korean',
        'star',
        'special',
    ],
    data() {
        return {
            receiveData:null
        }
    },
    mounted() {

    },
    methods: {

    },
    created() {
        // 형제 컴포넌트에서 값을 받는 리스너 .. eventBus.$on('보낸요청값' ,(date) => {})
        eventBus.$on('menuSended' ,(date) => {
            // menuSended를 통해 받은 데이터트 값을 받음
            this.receiveDate = date
        })
    }
}
</script>

```



```vue
{
    "rules": {
        ".read": true,
        ".write": true
    }
}

----

var database = firebase.database();
var ref = database.ref('scores');

var data = {
	name: "DTS",
	score: 43
}
ref.push(data);
```


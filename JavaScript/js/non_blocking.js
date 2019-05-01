// const nothing = () => {}

// console.log('start sleeping')
// setTimeout(nothing, 3000)   // non-block ----> callback stack
// console.log('end of program')

// python code 처럼 동작하게 하려면
// const logEnd = () => {
//     console.log('end of program')
// }
// console.log('start sleeping')
// setTimeout(logEnd, 3000)

// function first() {
//     console.log('first')
// }

// function second() {
//     console.log('second')
// }

// function third() {
//     console.log('third')
// }

// first()
// setTimeout(second, 1000)
// third()

// // 호출되는 순서는
// // first
// // third
// // second

// first()
// setTimeout(second, 0)   // 0초라도 제일 마지막에 호출되는 이유는 대기열에 들어가기 때문인다.
// third()

// 호출되는 순서는
// first
// third
// second

// func1()를 호출 했을 때 아래와 같이 콘솔에 출력
function func1() {
    console.log('func1')
    func2()
}
function func2() {
    setTimeout(() => console.log('func2'), 0)
    func3()
}
function func3() {
    console.log('func3')
}

func1()
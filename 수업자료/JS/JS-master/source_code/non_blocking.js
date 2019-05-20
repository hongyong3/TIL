const nothing = () => {}

console.log('start sleeping')
setTimeout(nothing, 3000) // non-block callback stack
console.log('end of program')

// python code 처럼 동작하게 하려면
const logEnd = () => {
    console.log('end of program')
}
console.log('start sleeping')
setTimeout(logEnd, 3000)


function first() {
    console.log('first')
}
function second() {
    console.log('second')
}
function third() {
    console.log('third')
}
first()
setTimeout(second, 5000)
third()


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








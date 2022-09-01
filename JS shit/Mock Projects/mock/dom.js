//class
class Person{
    constructor(name){
        this.name= name
    }

    output(){
        return this.name;
    }
}

let j=new Person('Jongseong')
const name=j.output();
console.log(Person instanceof Object)

let group= class{
    constructor(name){
        this.setName(name);
    }

    getName(){
        return this.name
    }

    setName(newName){
        newName= newName.trim()
        if(newName== ' '){
            throw 'EMPTY NAME';
        }
        this.name= newName
    }
}

let g= new  group('ENHYPEN')
console.log(g.getName())
g.setName('ENGENE')
console.log(g.getName())
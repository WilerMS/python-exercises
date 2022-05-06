num = 1
printer("Numero " + num)
printer(`Numero ${num}`)

const generar = (persona) => {
    console.log(persona['nombre'] + " " + persona["apellido"])
    console.log(`${persona.nombre} ${persona.apellido}`)
}

const generar = ({nombre, apellido}) => {
    console.log(`${nombre} ${apellido}`)
}
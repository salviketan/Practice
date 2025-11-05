// ##### Functions
fn main() {
    println!("Hello, world!");
    another_function(5);
    print_labeled_measurement(5, 'h');

    // 2. Statements and Expressions
    // let x = (let y = 6);        Statements do not return values
    
    /* 3. Calling a function is an expression. Calling a macro is an expression. 
    A new scope block created with curly brackets is an expression. */
    let y = {
        let x = 3;
        x + 1
    };
    println!("The value of y is: {y}");

    let x = five();
    println!("The value of x is: {x}");

    let x = plus_one(5);
    println!("The value of x is: {x}");
}
// 1. Parameters
fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}

// 4. Functions with Return Values
fn five() -> i32 {
    5
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
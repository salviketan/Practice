use std::io;


fn main() {
    // Data Types
    // Scalar Types
    // ##### Integer Types
    let x: u8 = 10;
    let y: i8 = -10;
    println!("u8 {x}, i8 {y}");

    // ##### Floating-Point Types
    let x: f64 = 2.23555555555;
    let y: f32 = 3.23555555;
    println!("f64 {x}, f32 {y}");

    // ##### Numeric Operation
    // addition
    let sum = 5 + 10;
    println!("addition {sum}");
    // subtraction
    let difference = 95.5 - 4.3;
    println!("subtraction {difference}");
    // multiplication
    let product = 4 * 30;
    println!("multiplication {product}");
    // division
    let quotient = 56.6 / 32.2;
    let truncated = -5 / 3; // Result in -1
    println!("division: quotient {quotient}, truncated {truncated}");
    // remainder
    let remainder = 43 % 5;
    println!("remainder {remainder}");

    // ##### boolean Types
    let x = true;
    let y: bool = false; // with explicit type annotation
    println!("x {x}, y {y}");

    // ##### The Character Type
    let c = 'z';
    let z: char = 'Z';  // with explicit type annotation
    let heart_eyed_cat = '😻';
    
    println!("c {c}, z char {z}, heart_eyed_cat {heart_eyed_cat}");

    // ##### Compound Types
    // ***** The Tuple Type
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x , y, z) = tup;
    println!("The value of x is {x}, y is {y}, z is {z}");

    let five_hundred = tup.0;
    let six_point_four = tup.1;
    let one = tup.2;
    println!("0 {five_hundred}, 1 {six_point_four}, 2 {one}");

    // ***** The Array Type
    let a = [1,2,3,4,5];
    println!("a {:?}", a);

    let a = [3; 5];
    println!("a {:?}", a);

    let a: [i32; 5] = [1, 2, 3, 4, 5];
    println!("a {:?}", a);

    // Accessing Array Elements
    let first = a[0];
    let second = a[1];

    println!("Access Array Elements {first}, {second}");

    // Invalid Array Element Access
    println!("Please enter an array index.");

    let mut index = String::new();

    io::stdin()
        .read_line(&mut index)
        .expect("Failed to read line");
    let index: usize = index
        .trim()
        .parse()
        .expect("Index entered was not a number");

    let element = a[index];

    println!("The value of the element at index {index} is: {element}");
}

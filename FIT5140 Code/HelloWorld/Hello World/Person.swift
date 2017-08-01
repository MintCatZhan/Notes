//
//  Person.swift
//  Hello World
//
//  Created by YuanZhan on 31/7/17.
//  Copyright © 2017 YuanZhan. All rights reserved.
//

import UIKit

class Person: NSObject {
    var name: String?
    var age: Int?
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
    
    func sayHello() -> String{
        return "Hello \(name!). You are \(age!) years old."
    }
}

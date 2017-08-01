//
//  ViewController.swift
//  Hello World
//
//  Created by YuanZhan on 31/7/17.
//  Copyright © 2017 YuanZhan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var inputName: UITextField!
    @IBOutlet weak var inputAge: UITextField!
    
    @IBAction func selectButton() {
        var messageString: String = "Not all fields were filled in!"
        
        if inputName.text != "" && inputAge.text != "" {
            //do something if it's not empty
            let constantName = inputName.text
            let constantAge = Int(inputAge.text!)
            let Person1 = Person(name: constantName!, age: constantAge!)
            messageString = Person1.sayHello()
        }
        
        
        // Setup an alert to show user details about the Person 
        // UIAlertController manages an alert instance
        let alertController = UIAlertController(title: "Alert", message: messageString, preferredStyle: UIAlertControllerStyle.alert)
        alertController.addAction(UIAlertAction(title: "Dismiss", style: UIAlertActionStyle.default, handler: nil))
        self.present(alertController, animated: true, completion: nil)
        
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}


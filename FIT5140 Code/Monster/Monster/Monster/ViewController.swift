//
//  ViewController.swift
//  Monster
//
//  Created by YuanZhan on 1/8/17.
//  Copyright © 2017 YuanZhan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var nameTextField: UITextField!
    @IBOutlet weak var levelTextField: UITextField!
    @IBOutlet weak var typeSegmentView: UISegmentedControl!
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Check the label of segue
        if (segue.identifier == "createMonsterSegue") {
            let name = nameTextField.text
            let level = Int(levelTextField.text!)
            var type: String?
            
            switch typeSegmentView.selectedSegmentIndex {
            case 0:
                type = "Fire"
                break
            case 1:
                type = "Grass"
                break
            case 2:
                type = "Water"
                break
            case 3:
                type = "Rock"
                break
            case 4:
                type = "Electric"
                break
            default:
                type = "Normal"
                break
            }
            
            let monster = Monster(name: name!, type: type!, level: level)
            
            // Try and cast destination as a ViewMonsterController object
            if let destinationVC = segue.destination as? ViewMonsterController{
                destinationVC.currentMonster = monster
            }
        }
    }

}


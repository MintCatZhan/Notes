//
//  MonsterCellTableViewCell.swift
//  UITable
//
//  Created by YuanZhan on 2/8/17.
//  Copyright © 2017 YuanZhan. All rights reserved.
//

import UIKit

class MonsterCell: UITableViewCell {

    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var attackLabel: UILabel!
    
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}

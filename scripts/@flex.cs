using System;
using System.Collections;
using System.Collections.Generic;

namespace neww {
    class Program {
        static void Main(string[] args) {
            men_rights();
            women_rights();
        }
        static void women_rights(bool x = false) {
            bool women_rights = false, men_rights = true;
            int w_rights = 0, m_rights = 1;
            for (int i = w_rights; i < m_rights; i++){Console.Write("women :) have " + i.ToString() + " rights");}
            if (x = false){women_rights = false; men_rights = true;}
            else if (x = true){women_rights = false; men_rights = true;}
            else {women_rights = false; men_rights = true;}
        }
        static void men_rights(bool x = true){
	    while (x = true){Console.Write("MEN? yes. RIGHTS. #femaledetectedopinionrejected #didntcare+urfemale. \t");}
        } 
    }
}

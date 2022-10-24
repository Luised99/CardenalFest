package com.example.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.db.querys.Querys;

@RequestMapping("/")
public class Controller {
	
	Querys querys;
	
	public Controller(Querys querys) {
		this.querys=querys;
	}
	
	@PostMapping("/autenticar")
	public void autenticar(@RequestParam("user")String user, @RequestParam("password")String password) {
		boolean auth = querys.autenticar(user, password);
		
		if(auth==true) {
			
		}
	}
	
	@PostMapping("/registro")
	public void registro(@RequestParam("user")String user, @RequestParam("password")String password) {
		querys.registro(user, password);
	}
}

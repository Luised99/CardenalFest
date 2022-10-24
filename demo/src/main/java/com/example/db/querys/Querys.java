package com.example.db.querys;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import org.springframework.stereotype.Component;

import com.example.db.config.DBConfig;

@Component
public class Querys {
	
	DBConfig dbConfig;
	Connection con;
	
	public Querys (DBConfig dbConfig) {
		this.dbConfig=dbConfig;
	}
	
	public boolean autenticar(String user, String password) {
		boolean exist = false;
		
		con = dbConfig.conectar();
	
		Statement stmt;
		try {
			stmt = con.createStatement();
			ResultSet rs=stmt.executeQuery("select * from usuario where user=" + user + " and password=" + password);
			if(rs.next() != false) {
				exist = true;
			}
			
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}  
		
		
		return exist;
	}
	
	public boolean registro(String user, String password) {
		boolean exist = false;
		
		con = dbConfig.conectar();
	
		Statement stmt;
		try {
			stmt = con.createStatement();
			ResultSet rs=stmt.executeQuery("select id from usuario where user=" + user + " and password=" + password);
			if(rs.next() != false) {
				exist = true;
			}
			
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}  
		
		
		return exist;
	}
}

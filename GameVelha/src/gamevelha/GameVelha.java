package gamevelha;

import java.util.Scanner;

public class GameVelha {
    public static void main(String[] args) {
        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
        System.out.println("|\tJogo da Velha\t\t|");
        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
        
        Scanner entrada = new Scanner(System.in);
        
        byte jogada = 0;
        
        String V = "0", primeiro = "0", segundo = "0", terceiro = "0", quarto = "0", quinto = "0", sexto = "0", setimo = "0", oitavo = "0", nono = "0", peca = "", pecaM = "", casa = "";
        
        primeiro = "1";
        segundo = "2";
        terceiro = "3";
        quarto = "4";
        quinto = "5";
        sexto = "6";
        setimo = "7";
        oitavo = "8";
        nono = "9";
        
        while(!"x".equals(peca) || !"o".equals(peca)) {
            System.out.print("Entre com a peça: ");
            peca = entrada.nextLine().toLowerCase();
            if("x".equals(peca)) {
                System.out.println("Sua peça é X");
                pecaM = "o";
                break;
            } else if("o".equals(peca)) {
                System.out.println("Sua peça é O");
                pecaM = "x";
                break;
            } else {
                System.out.println("Digite um valor correto como peça!");
            }
        }
        
        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
        System.out.println("|\tTabuleiro\t\t|");
        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
        System.out.println("\t1\t2\t3\n\t4\t5\t6\n\t7\t8\t9");
        
        while(jogada != 9) {
            if ((jogada % 2) == 0) {
                while (true) {
                    System.out.println("Sua peça: " + peca.toUpperCase());
                    System.out.print("Escolha a casa: ");
                    casa = entrada.nextLine();
                    if (casa == primeiro) {
                        primeiro = casa;
                        break;
                    } else if (casa == segundo) {
                        segundo = casa;
                        break;
                    } else if (casa == terceiro) {
                        terceiro = casa;
                        break;
                    } else if (casa == quarto) {
                        quarto = casa;
                        break;
                    } else if (casa == quinto) {
                        quinto = casa;
                        break;
                    } else if (casa == sexto) {
                        sexto = casa;
                        break;
                    } else if (casa == setimo) {
                        setimo = casa;
                        break;
                    } else if (casa == oitavo) {
                        oitavo = casa;
                        break;
                    } else if (casa == nono) {
                        nono = casa;
                        break;
                    }
                }
            } else {
                while (true) {
                    System.out.println("Sua peça: " + pecaM.toUpperCase());
                    System.out.print("Escolha a casa: ");
                    casa = entrada.nextLine();
                    if (casa == primeiro) {
                        primeiro = casa;
                        break;
                    } else if (casa == segundo) {
                        segundo = casa;
                        break;
                    } else if (casa == terceiro) {
                        terceiro = casa;
                        break;
                    } else if (casa == quarto) {
                        quarto = casa;
                        break;
                    } else if (casa == quinto) {
                        quinto = casa;
                        break;
                    } else if (casa == sexto) {
                        sexto = casa;
                        break;
                    } else if (casa == setimo) {
                        setimo = casa;
                        break;
                    } else if (casa == oitavo) {
                        oitavo = casa;
                        break;
                    } else if (casa == nono) {
                        nono = casa;
                        break;
                    }
                }
            }
        }    
    }
}
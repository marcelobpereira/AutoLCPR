import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;


public class projetoInterface extends Application {

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("AutoLCPR");

        // Criar o cabeçalho
        Label headerLabel = new Label("AutoLCPR");
        Label producerNameLabel = new Label("Nome do Produtor");
        VBox header = new VBox(headerLabel, producerNameLabel);

        // Criar os botões do menu lateral
        Button importarButton = new Button("Importar");
        Button receitasButton = new Button("Receitas");
        Button despesasButton = new Button("Despesas");
        Button rebanhoButton = new Button("Rebanho");
        Button relatoriosButton = new Button("Relatórios");
        Button produtorButton = new Button("Produtor");

        VBox menu = new VBox(importarButton, receitasButton, despesasButton, rebanhoButton, relatoriosButton, produtorButton);

        // Criar a área de conteúdo principal
        BorderPane mainContent = new BorderPane();
        mainContent.setTop(header);
        mainContent.setLeft(menu);

        // Configurar e exibir a cena
        Scene scene = new Scene(mainContent, 800, 600);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
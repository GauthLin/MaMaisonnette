<!DOCTYPE html>
<html>
    <head>
        <title>ECAM Project</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <?php include("header.php"); ?>

        <p class="FirstQuestion">
            <?php echo "Quelle pièce voulez-vous contrôler ?"; ?>
        </p>

        <div class="Piece">
            <div class="piece-info">
                <a href="chambre1.php">
                    <img class="Chambre1" src="Images/chambre_1.jpg" alt="Chambre 1"/>
                </a>
                <p>
                    <?php echo "Chambre1"; ?>
                </p>
            </div>
        </div>

        <div class=Piece>
            <div class="piece-info">
                <a href="chambre2.php">
                    <img class="Chambre2" src="Images/chambre_2.jpg" alt="Chambre 2"/>
                </a>
                <p>
                    <?php echo "Chambre2"; ?>
                </p>
            </div>
        </div>

        <div class=Piece>
            <div class="piece-info">
                <a href="salon.php">
                    <img class="Salon" src="Images/salon.jpg" alt="Salon"/>
                </a>
                <p>
                    <?php echo "&nbsp; &nbsp; Salon"; ?>
                </p>
            </div>
        </div>

        <div class=Piece>
            <div class="piece-info">
                <a href="maison.php">
                    <img class="Maison" src="Images/maison.jpg" alt="Maison"/>
                </a>
                <p>
                    <?php echo " &nbsp; &nbsp; Maison"; ?>
                </p>
            </div>
        </div>

    </body>
</html>
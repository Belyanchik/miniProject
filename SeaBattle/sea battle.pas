program sea_battle_by_belyanchik;

uses CRT; //Module for working with the console

var myfield : array [1..5, 1..5] of integer;
    opfield : array [1..5, 1..5] of integer;
    forprint : array [1..5, 1..5] of integer;
    i : integer;
    x, y : integer;
    countme, countop : integer;
    playstep : boolean;
    gameover : boolean;
    lastresult : string;
    
begin
    writeln('Your field:');
    writeln('  1 2 3 4 5');
    For i:=1 To 5 Do
      writeln(i, myfield[i]);
    countme := 1;
    
    While countme <= 5 Do //Filling in the field by the player
      begin
        writeln();
        writeln('Choose where to put the ship ', countme,'/5');
        write('Line = ');
        readln(x);
        if (x <= 5) and (x > 0)
          then
            begin
              write('Column = ');
              readln(y);
              if (y <= 5) and (y > 0)
                then
                  begin
                    if(myfield[x, y] = 0)
                    then
                      begin
                        myfield[x, y] := 1;
                        countme := countme + 1;
                        ClrScr; //Cleaning the console using the CRT module
                        writeln();
                        writeln('  1 2 3 4 5');
                        For i:=1 To 5 Do
                         writeln(i, myfield[i]);
                      end
                    else
                      begin
                        writeln();
                        writeln('This position is already occupied, try another one');
                      end;
                  end
                else
                  writeln('The column does not fit the range');
            end
          else
            writeln('The line does not fit the range');
    end;
    
    countop := 1; //Filling in the field by computer
    while countop <=5 do
      begin
        x := random(5);
        x := x + 1;
        y := random(5);
        y := y + 1;
        if(opfield[x, y] = 0)
          then
            begin
              opfield[x, y] := 1;
                countop := countop + 1;
            end
      end;
      
      countme := 5;
      countop := 5;
      playstep := true;
      ClrScr;
      writeln();
      writeln('Your field: ', countme, '/5');
      writeln('  1 2 3 4 5');
      For i:=1 To 5 Do
       writeln(i, myfield[i]);
      writeln();
      writeln('Opponent`s field:', countop, '/5');
      writeln('  1 2 3 4 5');
      For i:=1 To 5 Do
       writeln(i, forprint[i]);
      
      gameover := false; //The beginning of the game
      while gameover = false do
        begin
          if playstep = true //Player's move
            then
              begin
                writeln();
                writeln('Your move!');
                writeln();
                write('Line = ');
                readln(x);
                if (x <= 5) and (x > 0)
                  then
                    begin
                      write('Column = ');
                      readln(y);
                      if (y <= 5) and (y > 0)
                        then
                          begin
                            if opfield[x, y] = 0
                              then
                                begin
                                  ClrScr;
                                  opfield[x, y] := 2;
                                  forprint[x,y] := 2;
                                  playstep := false;
                                  lastresult := 'Miss!';
                                end
                              else if opfield[x, y] = 1
                                then
                                  begin
                                    ClrScr;
                                    opfield[x, y] := 2;
                                    forprint[x,y] := 2;
                                    lastresult := 'Hit!';
                                    countop := countop - 1
                                  end
                                else if opfield[x, y] = 2
                                  then
                                    begin
                                      ClrScr;
                                      writeln('You`ve already shot at this area');
                                      lastresult := '';
                                    end;
                          end
                        else
                          begin
                            ClrScr;
                            writeln('The column does not fit the range');
                            lastresult := '';
                          end;
                    end
                  else
                    begin
                      ClrScr;
                      writeln('The line does not fit the range');
                      lastresult := '';
                    end;
              end
              
            else //Computer move
              begin
                x := random(5);
                x := x + 1;
                y := random(5);
                y := y + 1;
                if myfield[x,y] = 0
                  then
                    begin
                      ClrScr;
                      myfield[x,y] := 2;
                      playstep := true;
                    end
                  else if myfield[x,y] = 1
                    then
                      begin
                        ClrScr;
                        myfield[x,y] := 2;
                        countme := countme - 1
                      end;
              end;
              
            writeln(lastresult); //Printing the current playing field
            writeln();
            writeln('Your field: ', countme, '/5');
            writeln('  1 2 3 4 5');
            For i:=1 To 5 Do
             writeln(i, myfield[i]);
            writeln();
            writeln('Opponent`s field:', countop, '/5');
            writeln('  1 2 3 4 5');
            For i:=1 To 5 Do
             writeln(i, forprint[i]);
            
            if countme = 0 //End-of-game check
              then
                gameover := true
              else if countop = 0
                then
                  gameover := true
        end;
        
      if countme = 0 //Announcement of the winner
        then
          begin
            ClrScr;
            writeln('The computer won!')
          end
        else
          begin
            ClrScr;
            writeln('The player won!')
          end;
end.
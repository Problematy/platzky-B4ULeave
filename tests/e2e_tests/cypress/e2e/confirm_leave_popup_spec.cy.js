describe('B4ULeave plugin exit intent', () => {
    beforeEach(() => {
        cy.visit('/');
    });

    it('shows modal when mouse leaves window (exit intent)', () => {
        cy.window().then((win) => {
            const event = new win.MouseEvent('mouseout', {
                bubbles: true,
                cancelable: true,
                relatedTarget: null
            });
            win.document.dispatchEvent(event);
        });

        cy.get('#B4ULeave-ModalWindow').should('be.visible');
        cy.contains('Stay').should('exist');
        cy.contains('Leave').should('exist');
        cy.get('#B4ULeave-Stay').click();
        cy.get('#B4ULeave-ModalWindow').should('not.be.visible');
    });

    it('changes URL after clicking Leave', () => {
        //save the initial url before triggering the exit intent
        cy.url().then((initialUrl) => {
            cy.window().then((win) => {
                const event = new win.MouseEvent('mouseout', {
                    bubbles: true,
                    cancelable: true,
                    relatedTarget: null
                });
                win.document.dispatchEvent(event);
            });

            cy.get('#B4ULeave-Leave').click();
            
            // verify the url has changed
            cy.url().should((newUrl) => {
                expect(newUrl).not.to.eq(initialUrl);
            });
        });
    });
    
});